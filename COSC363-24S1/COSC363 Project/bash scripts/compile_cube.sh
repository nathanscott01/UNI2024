#!/bin/bash

# Compile Cube.cpp with g++
g++ -Wall -o cube I_Cube/Cube.cpp -lm -lGL -lGLU -lglut -lGLEW

# Run the compiled executable
./cube


