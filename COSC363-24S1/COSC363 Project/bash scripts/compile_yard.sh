#!/bin/bash

# Compile Yard.cpp with g++
g++ -Wall -o yard II_Yard/Yard.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./yard

