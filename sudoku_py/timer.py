from time import clock
import functools


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = clock()
        return self

    def __exit__(self, *args):
        self.end = clock()
        self.secs = self.end - self.start
        self.ms = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.ms)


def calculate_time(verbose):
    def wrapper_func(func):
        @functools.wraps(func)
        def wrapper_args(_sudoku):
            start = clock()
            func(_sudoku)
            end = clock()
            secs = end - start
            ms = secs * 1000
            if verbose:
                print('elapsed time: %f ms' % ms)
        return wrapper_args
    return wrapper_func
