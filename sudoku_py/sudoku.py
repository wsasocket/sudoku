from point import Point


class Sudoku(object):

    def __init__(self):
        self._list = []
        self._to_be_filled = []
        for r in range(0, 9):
            for c in range(0, 9):
                p = Point(r, c)
                self._list.append(p)

    def __str__(self):
        return '%d Points in Sudoku' % len(self._list)

    @property
    def points(self):
        return self._to_be_filled

    def load_data_from_file(self, _path='/home/james/sudoku.txt'):
        index = 0
        with open(_path, 'r') as f:
            for row in range(0, 9):
                line = f.readline()
                for v in line[0:9]:
                    self._list[index].value = int(v)
                    index += 1

    def load_data_from_argv(self, _data=''):
        if len(_data) != 81:
            return
        index = 0
        v = [x for x in range(0, 10)]
        for i in _data:
            if int(i) not in v:
                return
        for i in _data:
            self._list[index].value = int(i)
            index += 1

    def print_sudoku(self, stdout=False):
        if stdout:
            for p in self._list:
                print(p.value, end='')
            print('')
            return
        print(' -------------------------------------')
        index = 0
        for p in self._list:
            if index % 3 == 0:
                print(' | ', end='')
            else:
                print('   ', end='')
            print(p.value, end='')
            if (index+1) % 9 == 0:
                if(index + 1) % 27 == 0:
                    print(' |\n +-----------+-----------+-----------+')
                else:
                    print(' |\n - --------- - --------- - --------- -')
            index += 1

    def get_value(self, index):
        return self._list[index].value

    def set_av(self, index, value):
        self._list[index].av = value

    def get_row_col_id(self, index):
        return self._list[index].row, self._list[index].col, self._list[index].id

    def get_row_values(self, row):
        tmp = [p.value for p in self._list if p.row == row]
        return set(tmp)

    def get_col_values(self, col):
        tmp = [p.value for p in self._list if p.col == col]
        return set(tmp)

    def get_cell_values(self, ids):
        tmp = [p.value for p in self._list if p.id == ids]
        return set(tmp)

    def pre_calculate(self):
        l = [i for i in range(1, 10)]
        for index in range(0, 81):
            if self.get_value(index) != 0:
                continue
            row, col, ids = self.get_row_col_id(index)
            set_row = self.get_row_values(row)
            set_col = self.get_col_values(col)
            set_id = self.get_cell_values(ids)
            sets = set_row | set_col | set_id
            av_set = set(l) - sets
            # 判断语句很重要，能大幅度减少运行时间
            if len(av_set) == 1:
                self._list[index].value = list(av_set)[0]
                continue
            self.set_av(index, av_set)
            self._to_be_filled.append(self._list[index])
        return self._to_be_filled

    def is_validate(self, index, value):

        row, col, ids = self.get_row_col_id(index)
        # 集合算法理论上不错，但是效率很低
        # set_row = self.get_row_values(row)
        # if value in set_row:
        #     return False
        # set_col = self.get_col_values(col)
        # if value in set_col:
        #     return False
        # set_id = self.get_cell_values(ids)
        # if value in set_id:
        #     return False
        # sets = set_row | set_col | set_id
        # if value not in sets:
        #     return True
        # return False
        # 遍历一下效率比集合运算高
        for p in self._list:
            if p.col == col or p.row == row or p.id == ids:
                if p.value == value:
                    return False
        return True

    def get_list_value(self):
        return [x.value for x in self._list]
