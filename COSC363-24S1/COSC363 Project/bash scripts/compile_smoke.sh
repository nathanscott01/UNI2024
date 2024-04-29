#!/bin/bash

# Compile SmokeParticles.cpp with g++
g++ -Wall -o smoke SmokeParticles.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./smoke

