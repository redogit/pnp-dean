#pragma once
#include "gyro/carrier.hpp"

namespace gyro {
class GraphCarrier final : public Carrier {
public:
    const char* name() const override { return "graph_carrier"; }
    CarrierProgress apply(State& state, CertificateLedger& ledger) override;
};
}
