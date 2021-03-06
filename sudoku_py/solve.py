"""recursive function"""
from sudoku import Sudoku
cursor = 0


def solve_sudoku(_sudoku):
    # 用于控制空点序列的游标
    global cursor
    # 终止的标准
    last_index = len(_sudoku.points)

    # 选择当前点
    _point = _sudoku.points[cursor]
    # 当前点可用值的序列
    av = _sudoku.points[cursor].av

    for value in av:
        if _sudoku.is_validate(_sudoku.points[cursor].index, value):
            # 如果选取的值可用，就设置值，并且开始处理下一个点
            _point.value = value
            cursor += 1
            if cursor == last_index:
                # 最后一个点处理完毕且正确就退出
                return 0
            # 递归调用
            ret = solve_sudoku(_sudoku)
            if ret == 0:
                return 0
            # 这部分是所有尝试失败后，将测试点置0
            _point.value = 0
            # 回退到前一个点
            cursor -= 1
    return -1


def sudoku_api(original):
    s = Sudoku()
    s.load_data_from_argv(original)
    cursor = 0
    s.pre_calculate()
    solve_sudoku(s)
    return s.get_list_value()
