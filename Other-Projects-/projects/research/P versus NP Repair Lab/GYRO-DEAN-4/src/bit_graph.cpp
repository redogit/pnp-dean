#include "gyro/dynamic_bitset.hpp"
#include "gyro/bit_graph.hpp"
#include "gyro/exact_rank.hpp"
#include <algorithm>
#include <sstream>
#include <limits>

namespace gyro {

DynamicBitset::DynamicBitset(std::size_t n, bool fill) : n_(n), words_((n + 63) / 64, fill ? ~0ULL : 0ULL) { clear_tail(); }
void DynamicBitset::set(std::size_t i) { if (i >= n_) throw std::out_of_range("bit"); words_[i/64] |= 1ULL << (i%64); }
void DynamicBitset::reset(std::size_t i) { if (i >= n_) throw std::out_of_range("bit"); words_[i/64] &= ~(1ULL << (i%64)); }
bool DynamicBitset::test(std::size_t i) const { if (i >= n_) throw std::out_of_range("bit"); return (words_[i/64] >> (i%64)) & 1ULL; }
std::size_t DynamicBitset::count() const noexcept { std::size_t c=0; for (auto w: words_) c += std::popcount(w); return c; }
bool DynamicBitset::any() const noexcept { for (auto w: words_) if (w) return true; return false; }
void DynamicBitset::check_compat(const DynamicBitset& rhs) const { if (n_ != rhs.n_) throw std::invalid_argument("bitset size mismatch"); }
DynamicBitset& DynamicBitset::operator&=(const DynamicBitset& rhs){ check_compat(rhs); for(std::size_t i=0;i<words_.size();++i) words_[i]&=rhs.words_[i]; return *this; }
DynamicBitset& DynamicBitset::operator|=(const DynamicBitset& rhs){ check_compat(rhs); for(std::size_t i=0;i<words_.size();++i) words_[i]|=rhs.words_[i]; clear_tail(); return *this; }
DynamicBitset DynamicBitset::operator&(const DynamicBitset& rhs) const { auto x=*this; x&=rhs; return x; }
DynamicBitset DynamicBitset::operator|(const DynamicBitset& rhs) const { auto x=*this; x|=rhs; return x; }
DynamicBitset DynamicBitset::minus(const DynamicBitset& rhs) const { check_compat(rhs); auto x=*this; for(std::size_t i=0;i<words_.size();++i) x.words_[i] &= ~rhs.words_[i]; x.clear_tail(); return x; }
std::vector<std::size_t> DynamicBitset::indices() const { std::vector<std::size_t> out; out.reserve(count()); for(std::size_t i=0;i<n_;++i) if(test(i)) out.push_back(i); return out; }
std::string DynamicBitset::key() const { std::ostringstream os; os<<std::hex; for(auto w:words_) os<<w<<','; return os.str(); }
void DynamicBitset::clear_tail(){ if(words_.empty() || n_%64==0) return; words_.back() &= ((1ULL<<(n_%64))-1ULL); }

BitGraph::BitGraph(std::size_t n) { adj_.reserve(n); for(std::size_t i=0;i<n;++i) adj_.emplace_back(n,false); }
void BitGraph::add_edge(std::size_t u,std::size_t v){ if(u==v) throw std::invalid_argument("self edge"); adj_.at(u).set(v); adj_.at(v).set(u); }
bool BitGraph::has_edge(std::size_t u,std::size_t v) const { return adj_.at(u).test(v); }
std::size_t BitGraph::induced_degree(std::size_t v,const DynamicBitset& active) const { return (adj_.at(v)&active).count(); }
std::size_t BitGraph::induced_compat_degree(std::size_t v,const DynamicBitset& active) const { auto c=active.count(); if(!active.test(v)) return 0; return c-1-induced_degree(v,active); }
bool BitGraph::is_independent(const std::vector<std::size_t>& vertices) const { for(std::size_t i=0;i<vertices.size();++i) for(std::size_t j=i+1;j<vertices.size();++j) if(has_edge(vertices[i],vertices[j])) return false; return true; }

std::size_t exact_rank_bareiss(IntegerMatrix m) {
    if (m.a.empty()) return 0;
    const std::size_t rows=m.a.size(), cols=m.a[0].size();
    std::size_t rank=0;
    std::int64_t prev=1;
    for(std::size_t col=0; col<cols && rank<rows; ++col){
        std::size_t pivot=rank;
        while(pivot<rows && m.a[pivot][col]==0) ++pivot;
        if(pivot==rows) continue;
        std::swap(m.a[pivot],m.a[rank]);
        auto p=m.a[rank][col];
        for(std::size_t i=rank+1;i<rows;++i){
            for(std::size_t j=col+1;j<cols;++j){
                __int128 num=(__int128)m.a[i][j]*p-(__int128)m.a[i][col]*m.a[rank][j];
                if(rank>0) num/=prev;
                if(num > std::numeric_limits<std::int64_t>::max() || num < std::numeric_limits<std::int64_t>::min())
                    throw std::overflow_error("Bareiss overflow: use big integer backend in production");
                m.a[i][j]=(std::int64_t)num;
            }
            m.a[i][col]=0;
        }
        prev=p;
        ++rank;
    }
    return rank;
}

}
