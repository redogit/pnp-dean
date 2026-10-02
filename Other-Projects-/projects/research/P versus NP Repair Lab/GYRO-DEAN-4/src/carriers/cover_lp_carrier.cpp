#include "gyro/carriers/cover_lp_carrier.hpp"
namespace gyro {
CarrierProgress CoverLpCarrier::apply(State&, CertificateLedger& ledger) {
    // Extension hook. The reference solver remains exact via branch fallback.
    // Only certificate-backed transformations should set changed=true.
    (void)ledger;
    return {};
}
}
