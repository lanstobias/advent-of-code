cmake_minimum_required(VERSION 3.5)
project(aoc2020)

add_executable(${CMAKE_PROJECT_NAME}
   src/main.cpp
)

#include_directories(${CMAKE_SOURCE_DIR}/include PUBLIC)

set(CMAKE_CXX_STANDARD 17)
target_compile_options(${CMAKE_PROJECT_NAME} PRIVATE
   -Wall -Werror -Wextra -Wpedantic
)

#target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC
   #${CMAKE_SOURCE_DIR}/include
#)
