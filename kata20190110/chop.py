class NotFound(Exception):
    pass


def _chop(n, l, start, num):
    if num == 1 and l[start] == n:
        return start
    elif num > 1:
        half = num // 2
        if n < l[start + half]:
            return _chop(n, l, start, half)
        else:
            return _chop(n, l, start + half, num - half)
    else:
        raise NotFound


def chop(n, l):
    try:
        return _chop(n, l, 0, len(l))
    except NotFound:
        return -1
