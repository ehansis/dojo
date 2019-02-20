c = lambda n, l: ((c(n, l[len(l) // 2:]), c(n, l[:len(l) // 2])[n < l[len(l) // 2]], 1)[l[0] == n], -1)[len(l) == 0]
# c = lambda n, l: ((c(n, l[len(l) // 2:]), c(n, l[:len(l) // 2])[n < l[len(l) // 2]], 1)[l[0] == n], -1)[len(l) == 0]
