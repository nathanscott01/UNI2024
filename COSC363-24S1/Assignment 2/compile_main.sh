#!/bin/bash

# Compile RayTracer.cpp, SceneObject.cpp and Sphere.cpp with g++
g++ -Wall -o main main.cpp Ray.cpp SceneObject.cpp Sphere.cpp Plane.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./main

