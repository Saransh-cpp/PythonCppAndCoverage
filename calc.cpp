#include <pybind11/pybind11.h>

namespace py = pybind11;

int multiply(int i, int j) {
    return i * j;
}

int add(int i, int j) {
    return i + j;
}

int subtract(int i, int j) {
    return i - j;
}

int divide(int i, int j) {
    return i / j;
}

float multiply(float i, float j) {
    return i * j;
}

float add(float i, float j) {
    return i + j;
}

float subtract(float i, float j) {
    return i - j;
}

float divide(float i, float j) {
    return i / j;
}

PYBIND11_MODULE(calc, m) {
    m.doc() = "Calculator example";

    m.def("multiply", py::overload_cast<int, int>(&multiply)    , "Multiplies two numbers");
    m.def("multiply", py::overload_cast<float, float>(&multiply), "Multiplies two numbers");
    m.def("add"     , py::overload_cast<int, int>(&add)         , "Adds two numbers");
    m.def("add"     , py::overload_cast<float, float>(&add)     , "Adds two numbers");
    m.def("subtract", py::overload_cast<int, int>(&subtract)    , "Subtracts two numbers");
    m.def("subtract", py::overload_cast<float, float>(&subtract), "Subtracts two numbers");
    m.def("divide"  , py::overload_cast<int, int>(&divide)      , "Multiplies two numbers");
    m.def("divide"  , py::overload_cast<float, float>(&divide)  , "Multiplies two numbers");
}
