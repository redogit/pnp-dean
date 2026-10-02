#pragma once
#include "gyro/carrier.hpp"

namespace gyro {
class CertifiedMpca final : public Carrier {
public:
    const char* name() const override { return "certified_mpca"; }
    CarrierProgress apply(State& state, CertificateLedger& ledger) override;
};
}
