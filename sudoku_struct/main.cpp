#include <iostream>
#include "Sudoku.hpp"
#include <sys/timeb.h>
using namespace std;

vector<shared_ptr<Point>>::iterator cursor;

long long getSystemTime() {
    struct timeb t;
    ftime(&t);
    return 1000 * t.time + t.millitm;
}

int solve(Sudoku &su) {
    vector<int> av = (*cursor)->av;
    for (auto v:av)
        if (su.Is_Validate((*cursor)->row, (*cursor)->col, v)) {
            (*cursor)->value = v;
            ++cursor;
            if (cursor == su.end())
                return 1;
            if (solve(su) == 1)
                return 1;
            (*cursor)->value = 0;
            --cursor;
        }
    return 0;
}

int main() {
    Sudoku sudoku;

    sudoku.Load_data();
    sudoku.PreCalculate();
    cursor = sudoku.begin();

    sudoku.Print();
    long long start = getSystemTime();
    solve(sudoku);
    long long finish = getSystemTime();
    sudoku.Print();

    cout << "Total run time: " <<finish-start<< " ms"<<endl;
    return 0;
}