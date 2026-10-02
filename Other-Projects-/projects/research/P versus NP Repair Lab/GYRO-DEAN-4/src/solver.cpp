#include "gyro/solver.hpp"
#include "gyro/carriers/graph_carrier.hpp"
#include "gyro/carriers/cover_lp_carrier.hpp"
#include "gyro/carriers/frame_hammer.hpp"
#include "gyro/carriers/certified_mpca.hpp"
#include "gyro/carriers/sat_consensus.hpp"
#include "gyro/carriers/factor_sql_carrier.hpp"
#include <algorithm>
#include <memory>
#include <stdexcept>

namespace gyro {

Solver::Solver(const BitGraph& graph):graph_(graph){}

SolveResult Solver::find_one(std::size_t q){
    memo_.clear();
    State s{&graph_, DynamicBitset(graph_.size(),true), q, {}, {}};
    return gyro(std::move(s));
}

bool Solver::verify(const std::vector<std::size_t>& cohort,std::size_t q,std::size_t capacity) const {
    if(q>capacity || cohort.size()!=q) return false;
    auto copy=cohort;
    std::sort(copy.begin(),copy.end());
    if(std::adjacent_find(copy.begin(),copy.end())!=copy.end()) return false;
    return graph_.is_independent(copy);
}

SolveResult Solver::find_with_forbidden(std::size_t q,const std::vector<std::size_t>& forbidden){
    memo_.clear();
    DynamicBitset c(graph_.size(),true);
    for(auto v:forbidden) if(v<graph_.size()) c.reset(v);
    State s{&graph_,std::move(c),q,{},forbidden};
    return gyro(std::move(s));
}

std::vector<std::vector<std::size_t>> Solver::find_up_to_four(std::size_t q,std::size_t capacity){
    std::vector<std::vector<std::size_t>> out;
    if(capacity<q) return out;
    auto first=find_one(q);
    if(!first.exists) return out;
    out.push_back(first.witness);

    while(out.size()<4){
        bool found=false;
        const std::size_t j=out.size();
        std::vector<std::size_t> idx(j,0);
        while(true){
            std::vector<std::size_t> forbid;
            forbid.reserve(j);
            for(std::size_t s=0;s<j;++s) forbid.push_back(out[s][idx[s]]);
            auto r=find_with_forbidden(q,forbid);
            if(r.exists){
                bool distinct=true;
                auto cand=r.witness; std::sort(cand.begin(),cand.end());
                for(auto prev:out){ std::sort(prev.begin(),prev.end()); if(prev==cand){ distinct=false; break; } }
                if(distinct){ out.push_back(std::move(r.witness)); found=true; break; }
            }
            std::size_t pos=0;
            for(;pos<j;++pos){ if(++idx[pos] < out[pos].size()) break; idx[pos]=0; }
            if(pos==j) break;
        }
        if(!found) break;
    }
    return out;
}

bool Solver::q_core_repair(State& s){
    bool any=false,changed=true;
    while(changed){
        changed=false;
        auto active=s.candidates.indices();
        for(auto v:active){
            if(graph_.induced_compat_degree(v,s.candidates)+1 < s.q){
                s.candidates.reset(v);
                s.forced_out.push_back(v);
                changed=any=true;
            }
        }
    }
    if(any) ledger_.add("graph","q-core","Removed candidates unable to belong to any q-independent-set by compatibility degree.");
    return any;
}

bool Solver::max_repair(State& s){
    bool any=false;
    while(true){
        bool changed=false;
        changed |= q_core_repair(s);
        if(s.q==0 || s.candidates.count()<s.q) return any||changed;

        // Exact isolate inclusion: an exclusion-isolated candidate is always safe to include.
        for(auto v:s.candidates.indices()){
            if(graph_.induced_degree(v,s.candidates)==0 && s.q>0){
                s.forced_in.push_back(v);
                s.candidates.reset(v);
                --s.q;
                changed=any=true;
                ledger_.add("graph","isolated-include","Included an exclusion-isolated candidate.");
                break;
            }
        }
        if(!changed) break;
    }
    return any;
}

std::size_t Solver::choose_pivot(const State& s) const {
    std::size_t best=graph_.size(), best_degree=0;
    for(auto v:s.candidates.indices()){
        auto d=graph_.induced_degree(v,s.candidates);
        if(best==graph_.size() || d>best_degree){ best=v; best_degree=d; }
    }
    if(best==graph_.size()) throw std::logic_error("no pivot");
    return best;
}

SolveResult Solver::branch(State s,std::size_t v){
    // Include branch first: remove v and all exclusion neighbors, decrement q.
    State in=s;
    auto nbrs=graph_.neighbors(v) & in.candidates;
    in.candidates=in.candidates.minus(nbrs);
    if(in.candidates.test(v)) in.candidates.reset(v);
    in.forced_in.push_back(v);
    if(in.q>0) --in.q;
    auto r=gyro(std::move(in));
    if(r.exists) return r;

    // Exclude branch.
    State out=s;
    out.candidates.reset(v);
    out.forced_out.push_back(v);
    return gyro(std::move(out));
}

SolveResult Solver::gyro(State s){
    max_repair(s);
    if(s.q==0) return {true,s.forced_in};
    if(s.candidates.count()<s.q) return {false,{}};

    const auto key=s.memo_key();
    if(auto it=memo_.find(key);it!=memo_.end()){
        auto r=it->second;
        if(r.exists){
            // Witness in memo is residual-only in this compact reference implementation;
            // avoid unsound reuse across different forced_in contexts.
        } else return r;
    }

    // Carrier loop. Advanced carriers are no-op hooks in the compact reference build;
    // production versions add only certificate-backed exact progress.
    std::vector<std::unique_ptr<Carrier>> carriers;
    carriers.emplace_back(std::make_unique<GraphCarrier>());
    carriers.emplace_back(std::make_unique<CoverLpCarrier>());
    carriers.emplace_back(std::make_unique<FrameHammer>());
    carriers.emplace_back(std::make_unique<CertifiedMpca>());
    carriers.emplace_back(std::make_unique<SatConsensus>());
    carriers.emplace_back(std::make_unique<FactorSqlCarrier>());

    bool progress=true;
    while(progress){
        progress=false;
        for(auto& c:carriers){
            auto p=c->apply(s,ledger_);
            if(p.terminal) return p.terminal_result;
            if(p.changed){ progress=true; max_repair(s); break; }
        }
    }

    if(s.q==0) return {true,s.forced_in};
    if(s.candidates.count()<s.q){ memo_[key]={false,{}}; return {false,{}}; }

    auto pivot=choose_pivot(s);
    auto r=branch(std::move(s),pivot);
    if(!r.exists) memo_[key]=r;
    return r;
}

}
