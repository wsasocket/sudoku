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

    def load_data(self, path='/home/james/sudoku.txt'):
        index = 0
        with open(path, 'r') as f:
            for row in range(0, 9):
                line = f.readline()
                for v in line[0:9]:
                    self._list[index].value = int(v)
                    index += 1

    def print_sudoku(self):
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
        for index in range(0, 81):
            if self.get_value(index) != 0:
                continue
            row, col, ids = self.get_row_col_id(index)
            set_row = self.get_row_values(row)
            set_col = self.get_col_values(col)
            set_id = self.get_cell_values(ids)
            sets = set_row | set_col | set_id
            l = [i for i in range(1, 10)]
            av_set = set(l) - sets
            self.set_av(index, av_set)
            self._to_be_filled.append(self._list[index])
        return self._to_be_filled

    def is_validate(self, index, value):

        row, col, ids = self.get_row_col_id(index)
        set_row = self.get_row_values(row)
        if value in set_row:
            return False
        set_col = self.get_col_values(col)
        if value in set_col:
            return False
        set_id = self.get_cell_values(ids)
        if value in set_id:
            return False
        sets = set_row | set_col | set_id

        if value not in sets:
            return True
        return False