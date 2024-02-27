#!/bin/bash

# Compile Teapot.cpp with g++
g++ -Wall -o model Model3D.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./model

