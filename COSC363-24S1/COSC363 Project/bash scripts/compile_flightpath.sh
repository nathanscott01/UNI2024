#!/bin/bash

# Compile FlightPath.cpp with g++
g++ -Wall -o flightpath I_FlightPath/FlightPath.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./flightpath

