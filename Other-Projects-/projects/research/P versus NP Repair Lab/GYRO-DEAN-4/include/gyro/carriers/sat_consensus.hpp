#pragma once
#include "gyro/carrier.hpp"

namespace gyro {
class SatConsensus final : public Carrier {
public:
    const char* name() const override { return "sat_consensus"; }
    CarrierProgress apply(State& state, CertificateLedger& ledger) override;
};
}
