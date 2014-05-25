import time


class Timer:
    def __init__(self):
        self.start_time = time.clock()

    def elapsed(self):
        return prettify(time.clock() - self.start_time)


def prettify(elapsed):
    hours, remainder = divmod(elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)

    strings = []
    _append_if_positive(strings, hours, 'hour')
    _append_if_positive(strings, minutes, 'minute')
    _append_if_positive(strings, seconds, 'second')

    return ', '.join(strings)


def _append_if_positive(strings, value, desc):
    if value > 0:
        strings.append('%s %s%s' % (_readable(value), desc, '' if value == 1 else 's'))


def _readable(value):
    if value < 1:
        return '%.3f' % value

    value_map = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
    }

    try:
        return value_map[int(value)]
    except KeyError:
        return '%d' % value
