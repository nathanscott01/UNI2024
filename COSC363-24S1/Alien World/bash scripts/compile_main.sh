#!/bin/bash

# Compile main.cpp with g++
g++ -Wall -o main main.cpp alien.cpp skybox.cpp floor.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./main
