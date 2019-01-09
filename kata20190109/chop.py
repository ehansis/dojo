def chop(n, l):
    if len(l) == 0:
        return -1
    elif len(l) == 1:
        if l[0] == n:
            return 0
        else:
            return -1
    else:
        half = len(l) // 2
        if n < l[half]:
            c = chop(n, l[:half])
            return c if c >= 0 else -1
        else:
            c = chop(n, l[half:])
            return c + half if c >= 0 else -1
