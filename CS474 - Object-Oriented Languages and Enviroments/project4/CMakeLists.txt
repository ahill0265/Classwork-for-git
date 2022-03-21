cmake_minimum_required(VERSION 3.13)
project(project4)

set(CMAKE_CXX_STANDARD 14)
set(Headers Instruction.h Assignment.h Calculate.h)

add_executable(project4 main.cpp Instruction.cpp Assignment.cpp Calculate.cpp)