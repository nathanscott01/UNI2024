#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o cannon Cannon.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./cannon

