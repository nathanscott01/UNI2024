#!/bin/bash

# Compile RayTracer.cpp, SceneObject.cpp and Sphere.cpp with g++
g++ -Wall -o raytracer RayTracer.cpp Ray.cpp SceneObject.cpp Sphere.cpp Plane.cpp TextureBMP.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./raytracer

