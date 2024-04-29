#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o shadow II_Shadow/Shadow.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./shadow

