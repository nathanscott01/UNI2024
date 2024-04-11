#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o humanoid_floor Humanoid_texture_floor.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./humanoid_floor

