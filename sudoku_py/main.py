from sudoku import Sudoku
from timer import Timer, calculate_time
import sys
from solve import solve_sudoku

if __name__ == '__main__':
    arg = sys.argv[1]

    sudoku = Sudoku()
    if arg is None:
        sudoku.load_data_from_file()

    if arg is not None:
        if arg.find('/') >= 0:
            sudoku.load_data_from_file(arg)
        else:
            sudoku.load_data_from_argv(arg)
    sudoku.print_sudoku(stdout=False)
    sudoku.pre_calculate()
    with Timer(True) as t:
        # cursor = 0
        solve_sudoku(sudoku)
    sudoku.print_sudoku(stdout=False)


