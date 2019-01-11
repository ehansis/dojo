def chop(n, l):
    start = 0
    num = len(l)

    while num > 1:
        half = num // 2
        if n < l[start + half]:
            num = half
        else:
            start += half
            num -= half

    if num == 1 and l[start] == n:
        return start
    else:
        return -1

