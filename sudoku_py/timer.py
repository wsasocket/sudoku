from time import clock


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