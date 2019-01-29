def chop(n, l):
    retval = -1
    if len(l) == 1 and l[0] == n:
            retval = 0
    elif len(l) > 1:
        half = len(l) // 2
        if n < l[half]:
            retval = chop(n, l[:half])
        else:
            c = chop(n, l[half:])
            if c > -1:
                retval = half + c

    return retval
