#pragma once
#include "gyro/carrier.hpp"

namespace gyro {
class FrameHammer final : public Carrier {
public:
    const char* name() const override { return "frame_hammer"; }
    CarrierProgress apply(State& state, CertificateLedger& ledger) override;
};
}
