from sudoku import Sudoku


def solve_sudoku(_sudoku):
    # 用于控制空点序列的游标
    global zeroPoint_index
    # 终止的标准
    last_index = len(_sudoku.points)

    # 选择当前点
    _point = _sudoku.points[zeroPoint_index]
    # 当前点可用值的序列
    av = _sudoku.points[zeroPoint_index].av

    for value in av:
        if sudoku.is_validate(_sudoku.points[zeroPoint_index].index, value):
            # 如果选取的值可用，就设置值，并且开始处理下一个点
            _point.value = value
            zeroPoint_index += 1
            if zeroPoint_index == last_index:
                # 最后一个点处理完毕且正确就退出
                return 0
            # 递归调用
            ret = solve_sudoku(_sudoku)
            if ret == 0:
                return 0
            # 这部分是所有尝试失败后，将测试点置0
            _point.value = 0
            # 回退到前一个点
            zeroPoint_index -= 1
    return -1

if __name__ == '__main__':

    sudoku = Sudoku()
    sudoku.load_data()
    sudoku.pre_calculate()
    sudoku.print_sudoku()

    zeroPoint_index = 0
    solve_sudoku(sudoku)
    sudoku.print_sudoku()