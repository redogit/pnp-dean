#pragma once
#include "gyro/dynamic_bitset.hpp"
#include <cstddef>
#include <utility>
#include <vector>

namespace gyro {

class BitGraph {
public:
    explicit BitGraph(std::size_t n = 0);
    std::size_t size() const noexcept { return adj_.size(); }

    void add_edge(std::size_t u, std::size_t v);
    bool has_edge(std::size_t u, std::size_t v) const;
    const DynamicBitset& neighbors(std::size_t v) const { return adj_.at(v); }

    std::size_t induced_degree(std::size_t v, const DynamicBitset& active) const;
    std::size_t induced_compat_degree(std::size_t v, const DynamicBitset& active) const;
    bool is_independent(const std::vector<std::size_t>& vertices) const;

private:
    std::vector<DynamicBitset> adj_;
};

}
