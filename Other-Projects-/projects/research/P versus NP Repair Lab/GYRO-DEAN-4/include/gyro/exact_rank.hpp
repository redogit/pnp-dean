#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>

namespace gyro {

// Exact rank interface used by the certified MPCA/Macaulay carrier.
// Production implementations should use fraction-free elimination or
// modular rank with exact verification. This reference project keeps the
// interface separate from heuristic floating-point PCA/SVD steering.
struct IntegerMatrix {
    std::vector<std::vector<std::int64_t>> a;
};

std::size_t exact_rank_bareiss(IntegerMatrix m);

}
