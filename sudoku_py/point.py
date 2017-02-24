"""
数独9X9 的每一个单位
"""


class Point(object):
    def __init__(self, row, col, value=0):
        self._row = row
        self._col = col
        self._id = int(row / 3) * 3 + int(col / 3)
        self._value = value
        self._index = row * 9 + col
        self._av = []

    def __str__(self):
        return 'row:%d col:%d cell_ID:%d value:%d' % (self._row, self._col, self._id, self._value)

    @property
    def index(self):
        return self._index

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def av(self):
        return self._av

    @av.setter
    def av(self, value):
        self._av = list(value)

