cmake_minimum_required(VERSION 3.6)
project(sudoku)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp Sudoku.cpp Sudoku.hpp )
add_executable(sudoku ${SOURCE_FILES})
