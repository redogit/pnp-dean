#include "gyro/carriers/frame_hammer.hpp"
namespace gyro {
CarrierProgress FrameHammer::apply(State&, CertificateLedger& ledger) {
    // Extension hook. The reference solver remains exact via branch fallback.
    // Only certificate-backed transformations should set changed=true.
    (void)ledger;
    return {};
}
}
