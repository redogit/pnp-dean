#pragma once
#include <string>
#include <vector>

namespace gyro {

struct CertificateEvent {
    std::string carrier;
    std::string theorem;
    std::string detail;
};

struct CertificateLedger {
    std::vector<CertificateEvent> events;
    void add(std::string carrier, std::string theorem, std::string detail) {
        events.push_back({std::move(carrier), std::move(theorem), std::move(detail)});
    }
};

}
