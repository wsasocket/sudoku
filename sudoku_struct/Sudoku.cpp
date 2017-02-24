//
// Created by james on 17-2-17.
//


#include <fstream>
#include <set>
#include <algorithm>
#include "Sudoku.hpp"

Sudoku::Sudoku() {
    _list = {};
    for (int r = 0; r < 9; ++r)
        for (int c = 0; c < 9; ++c) {
            shared_ptr<Point> p = make_shared<Point>();
            p->row = r;
            p->col = c;
            p->cell = r / 3 * 3 + c / 3;
            _list.push_back(p);
        }
}

Sudoku::~Sudoku() {

}

int Sudoku::Load_data(string filename) {

    ifstream file(filename);
    if (!file.is_open())
        return -1;
    string buffer(128, 0);
    int index = 0, row = 0;
    while (true) {
        file >> buffer;
        if (file.eof())
            break;
        if (buffer.length() != 9) {
            file.close();
            return -1;
        }
        for (auto c : buffer) {
            _list[index]->value = c - '0';
            ++index;
        }
        ++row;
    }
    file.close();
    return 0;
}

void Sudoku::PreCalculate() {
    /*
     * 预先计算一下，将需要填的点和对应可填的数据提取出来
     * */
    set<int> inter = {};
    vector<int> ret = {};
    set<int> full = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (auto p:_list) {
        if (p->value != 0)
            continue;
        set<int> r = Get_Row_set(p->row);
        set<int> c = Get_Col_set(p->col);
        set<int> l = Get_Cell_set(p->cell);
        set_union(r.begin(), r.end(), c.begin(), c.end(), inserter(inter, inter.end()));
        set_union(l.begin(), l.end(), ret.begin(), ret.end(), inserter(inter, inter.end()));
        set_difference(full.begin(), full.end(), inter.begin(), inter.end(), back_inserter(ret));
        // 如果可填的数值唯一就直接填写
        if (ret.size() == 0)
            p->value = ret[0];
        else {
            for (auto av_p:ret)
                p->av.push_back(av_p);
            _to_be_filled.push_back(p);
        }
        ret.clear();
        inter.clear();
    }
}

void Sudoku::Print() {
    int index = 0;
    cout << "Sudoku" << endl;
    cout << " -------------------------------------" << endl;
    for (auto p:_list) {
        //p 不是迭代器，是具体的元素，
        if (index % 3 == 0)
            cout << " | ";
        else
            cout << "   ";
        cout << p->value;
        if ((index + 1) % 9 == 0)
            if ((index + 1) % 27 == 0) {
                cout << " |" << endl;
                cout << " +===========+===========+===========+" << endl;
            } else {
                cout << " |" << endl;
                cout << " - --------- - --------- - --------- -" << endl;
            }
        ++index;
    }
}

set<int> Sudoku::Get_Row_set(int r) {
    set<int> _set;
    for (auto p:_list) {
        if (p->row == r) {
            if (p->value == 0)
                continue;
            _set.insert(p->value);
        }
    }
    return _set;
}

set<int> Sudoku::Get_Cell_set(int c) {
    set<int> _set;
    for (auto p:_list) {
        if (p->cell == c) {
            if (p->value == 0)
                continue;
            _set.insert(p->value);
        }
    }
    return _set;
}

set<int> Sudoku::Get_Col_set(int c) {
    set<int> _set;
    for (auto p: _list) {
        if (p->col == c) {
            if (p->value == 0)
                continue;
            _set.insert(p->value);
        }
    }
    return _set;
}

bool Sudoku::Is_Validate(int row, int col, int value) {
// 下面的代码非常的慢！！！
//    set<int> r = Get_Row_set(row);
//    auto meet_r = find_if(r.begin(), r.end(), [value](const int &v) { return value == v; });
//    if (meet_r != r.end())
//        return false;
//
//    set<int> c = Get_Col_set(col);
//    auto meet_c = find_if(c.begin(), c.end(), [value](const int &v) { return value == v; });
//    if (meet_c != c.end())
//        return false;
//
//    set<int> l = Get_Cell_set(row / 3 * 3 + col / 3);
//    auto meet_l = find_if(l.begin(), l.end(), [value](const int &v) { return value == v; });
//    return !(meet_l != l.end());
    for (auto p : _list) {
        if (row == p->row || col == p->col || (row / 3 * 3 + col / 3) == p->cell) {
            if (p->value == value)
                return false;
        }
    }
    return true;
}

vector<shared_ptr<Point>>::iterator Sudoku::begin() {
    return _to_be_filled.begin();
}

vector<shared_ptr<Point>>::iterator Sudoku::end() {
    return _to_be_filled.end();
}
