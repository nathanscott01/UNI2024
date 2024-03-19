#!/bin/bash

# Compile Eartb.cpp with g++
g++ -Wall -o walls I_Walls/Walls.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./walls


