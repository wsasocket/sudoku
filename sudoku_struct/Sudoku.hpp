//
// Created by james on 17-2-17.
//

#ifndef SUDOKU_SUDOKU_HPP
#define SUDOKU_SUDOKU_HPP

#include <iostream>
#include <vector>
#include <memory>
#include <set>
//#include "Point.hpp"

using namespace std;

typedef struct {
    int row;
    int col;
    int cell;
    int value;
    vector<int> av;
}Point;

class Sudoku {
public:
    virtual ~Sudoku();

    Sudoku();

    int Load_data(string filename = "/home/james/sudoku.txt");

    void PreCalculate();

    void Print();

    bool Is_Validate(int r,int c,int v);

    vector<shared_ptr<Point>>::iterator begin();

    vector<shared_ptr<Point>>::iterator end();

private:
    set<int> Get_Row_set(int r);
    set<int> Get_Cell_set(int c);
    set<int> Get_Col_set(int c);

private:
    vector<shared_ptr<Point>> _list;
    vector<shared_ptr<Point>> _to_be_filled;
};


#endif //SUDOKU_SUDOKU_HPP
