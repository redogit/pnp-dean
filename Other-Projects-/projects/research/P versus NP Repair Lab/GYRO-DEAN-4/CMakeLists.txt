cmake_minimum_required(VERSION 3.20)
project(GYRO_DEAN_4 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

enable_testing()

add_library(gyro_core
    src/bit_graph.cpp
    src/solver.cpp
    src/carriers/graph_carrier.cpp
    src/carriers/cover_lp_carrier.cpp
    src/carriers/frame_hammer.cpp
    src/carriers/certified_mpca.cpp
    src/carriers/sat_consensus.cpp
    src/carriers/factor_sql_carrier.cpp
)
target_include_directories(gyro_core PUBLIC include)

add_executable(gyro_dean src/main.cpp)
target_link_libraries(gyro_dean PRIVATE gyro_core)

add_executable(gyro_tests tests/test_solver.cpp)
target_link_libraries(gyro_tests PRIVATE gyro_core)
add_test(NAME gyro_tests COMMAND gyro_tests)

add_executable(gyro_exhaustive_tests tests/test_exhaustive.cpp)
target_link_libraries(gyro_exhaustive_tests PRIVATE gyro_core)
add_test(NAME gyro_exhaustive_tests COMMAND gyro_exhaustive_tests)
