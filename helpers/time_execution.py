import time


def time_execution(f):
    def timed(*args, **kw):
        start = time.time()
        result = f(*args, **kw)
        end = time.time()

        print '%r  %2.2f ms' % \
              (f.__name__, (start - end) * 1000)

        return result

    return timed
