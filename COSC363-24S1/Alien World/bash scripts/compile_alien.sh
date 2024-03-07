#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o alien alien.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./alien

