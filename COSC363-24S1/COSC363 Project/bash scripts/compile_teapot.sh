#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o teapot Teapot.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./teapot

