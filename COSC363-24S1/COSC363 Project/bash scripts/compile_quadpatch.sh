#!/bin/bash

# Compile Quadpatches.cpp with g++
g++ -Wall -o quadpatch I_QuadPatches/QuadPatches.cpp -lm -lGL -lGLU -lglut -lGLEW

# Run the compiled executable
./quadpatch

