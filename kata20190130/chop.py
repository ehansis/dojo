def chop(n, l):
    start = 0
    end = len(l)

    while end - start > 1:
        half = start + (end - start) // 2
        if n < l[half]:
            end = half
        else:
            start = half

    if end > start and l[start] == n:
        return start

    return -1
