import time


class Timer:
    def __init__(self):
        self.start_time = time.clock()

    def elapsed(self):
        return _prettify(time.clock() - self.start_time)


def _prettify(elapsed):
    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)

    strings = []
    _append_if_positive(strings, hours, 'hour')
    _append_if_positive(strings, minutes, 'minute')
    _append_if_positive(strings, seconds, 'second')

    return ', '.join(strings)


def _append_if_positive(strings, value, desc):
    if value > 0:
        strings.append('%d %s%s' % (value, desc, '' if value == 1 else 's'))
