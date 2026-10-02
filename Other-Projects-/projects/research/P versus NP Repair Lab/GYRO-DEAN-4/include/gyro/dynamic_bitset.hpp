#pragma once
#include <cstdint>
#include <vector>
#include <string>
#include <stdexcept>
#include <bit>

namespace gyro {

class DynamicBitset {
public:
    explicit DynamicBitset(std::size_t n = 0, bool fill = false);

    std::size_t size() const noexcept { return n_; }
    void set(std::size_t i);
    void reset(std::size_t i);
    bool test(std::size_t i) const;
    std::size_t count() const noexcept;
    bool any() const noexcept;
    bool none() const noexcept { return !any(); }

    DynamicBitset& operator&=(const DynamicBitset& rhs);
    DynamicBitset& operator|=(const DynamicBitset& rhs);
    DynamicBitset operator&(const DynamicBitset& rhs) const;
    DynamicBitset operator|(const DynamicBitset& rhs) const;
    DynamicBitset minus(const DynamicBitset& rhs) const;

    std::vector<std::size_t> indices() const;
    std::string key() const;

private:
    std::size_t n_{};
    std::vector<std::uint64_t> words_;
    void check_compat(const DynamicBitset& rhs) const;
    void clear_tail();
};

}
