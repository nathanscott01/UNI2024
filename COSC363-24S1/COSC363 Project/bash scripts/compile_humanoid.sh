#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o humanoid Humanoid.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./humanoid

