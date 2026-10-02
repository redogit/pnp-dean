#include "gyro/solver.hpp"
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>

static std::vector<std::string> split_csv(const std::string& s){
    std::vector<std::string> out; std::stringstream ss(s); std::string x;
    while(std::getline(ss,x,',')) out.push_back(x);
    return out;
}

int main(int argc,char** argv){
    std::string students_file, exclusions_file;
    std::size_t q=0, capacity=0;
    for(int i=1;i<argc;++i){
        std::string a=argv[i];
        if(a=="--students" && i+1<argc) students_file=argv[++i];
        else if(a=="--exclusions" && i+1<argc) exclusions_file=argv[++i];
        else if(a=="--q" && i+1<argc) q=std::stoull(argv[++i]);
        else if(a=="--capacity" && i+1<argc) capacity=std::stoull(argv[++i]);
    }
    if(students_file.empty()||exclusions_file.empty()||q==0||capacity==0){
        std::cerr<<"usage: gyro_dean --students students.csv --exclusions exclusions.csv --q N --capacity C\n";
        return 2;
    }

    std::ifstream sf(students_file); if(!sf){std::cerr<<"cannot open students\n";return 2;}
    std::unordered_map<std::string,std::size_t> id;
    std::vector<std::string> names;
    std::string line;
    while(std::getline(sf,line)){
        if(line.empty()||line.rfind("student_id",0)==0) continue;
        auto v=split_csv(line); if(v.empty()) continue;
        id[v[0]]=names.size(); names.push_back(v[0]);
    }
    gyro::BitGraph g(names.size());
    std::ifstream ef(exclusions_file); if(!ef){std::cerr<<"cannot open exclusions\n";return 2;}
    while(std::getline(ef,line)){
        if(line.empty()||line.rfind("a,",0)==0) continue;
        auto v=split_csv(line); if(v.size()<2) continue;
        if(id.count(v[0])&&id.count(v[1])) g.add_edge(id[v[0]],id[v[1]]);
    }

    gyro::Solver solver(g);
    auto results=solver.find_up_to_four(q,capacity);
    std::cout<<"results="<<results.size()<<"\n";
    for(std::size_t r=0;r<results.size();++r){
        std::cout<<"result "<<(r+1)<<":";
        for(auto v:results[r]) std::cout<<" "<<names[v];
        std::cout<<"\n";
    }
    return results.empty()?1:0;
}
