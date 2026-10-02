#pragma once
#include "gyro/carrier.hpp"

namespace gyro {
class FactorSqlCarrier final : public Carrier {
public:
    const char* name() const override { return "factor_sql_carrier"; }
    CarrierProgress apply(State& state, CertificateLedger& ledger) override;
};
}
