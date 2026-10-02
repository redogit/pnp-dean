#include "gyro/carriers/certified_mpca.hpp"
namespace gyro {
CarrierProgress CertifiedMpca::apply(State&, CertificateLedger& ledger) {
    // Extension hook. The reference solver remains exact via branch fallback.
    // Only certificate-backed transformations should set changed=true.
    (void)ledger;
    return {};
}
}
