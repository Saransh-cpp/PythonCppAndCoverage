cmake_minimum_required(VERSION 3.4)
project(pybind_demo)
set(CMAKE_CXX_STANDARD 14)	

add_subdirectory(pybind11)
pybind11_add_module(calc calc.cpp)
