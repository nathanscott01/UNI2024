#!/bin/bash

# Compile Toytrain.cpp and RailModels.cpp with g++
g++ -Wall -o toytrain I_ToyTrain/ToyTrain.cpp I_ToyTrain/RailModels.cpp -lm -lGL -lGLU -lglut

# Run the compiled executable
./toytrain

