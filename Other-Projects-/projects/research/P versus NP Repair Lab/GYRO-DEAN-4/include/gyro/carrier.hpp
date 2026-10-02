#pragma once
#include "gyro/state.hpp"
#include "gyro/certificate.hpp"

namespace gyro {

struct CarrierProgress {
    bool changed{false};
    bool terminal{false};
    SolveResult terminal_result{};
    std::size_t certified_rank_gain{0};
};

class Carrier {
public:
    virtual ~Carrier() = default;
    virtual const char* name() const = 0;
    virtual CarrierProgress apply(State& state, CertificateLedger& ledger) = 0;
};

}
