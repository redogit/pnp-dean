#pragma once
#include "gyro/carrier.hpp"

namespace gyro {
class CoverLpCarrier final : public Carrier {
public:
    const char* name() const override { return "cover_lp_carrier"; }
    CarrierProgress apply(State& state, CertificateLedger& ledger) override;
};
}
