#!/bin/bash

# Compile TeapotPatches.cpp with g++
g++ -Wall -o teapotpatch II_TeapotPatches/TeapotPatches.cpp -lm -lGL -lGLU -lglut -lGLEW

# Run the compiled executable
./teapotpatch

