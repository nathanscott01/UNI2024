#!/bin/bash

# Compile Eartb.cpp with g++
g++ -Wall -o earth III_Earth/Earth.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./earth


