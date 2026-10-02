#pragma once
#include "gyro/bit_graph.hpp"
#include "gyro/dynamic_bitset.hpp"
#include <cstddef>
#include <string>
#include <vector>

namespace gyro {

struct State {
    const BitGraph* graph{};
    DynamicBitset candidates;
    std::size_t q{};
    std::vector<std::size_t> forced_in;
    std::vector<std::size_t> forced_out;

    std::string memo_key() const {
        return std::to_string(q) + ":" + candidates.key();
    }
};

struct SolveResult {
    bool exists{false};
    std::vector<std::size_t> witness;
};

}
