#include "gyro/carriers/sat_consensus.hpp"
namespace gyro {
CarrierProgress SatConsensus::apply(State&, CertificateLedger& ledger) {
    // Extension hook. The reference solver remains exact via branch fallback.
    // Only certificate-backed transformations should set changed=true.
    (void)ledger;
    return {};
}
}
