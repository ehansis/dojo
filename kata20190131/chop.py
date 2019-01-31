chop = lambda n, l: -1 if len(l) == 0 \
    else (0 if len(l) == 1 and l[0] == n
          else (-1 if len(l) == 1 and l[0] != n
                else (chop(n, l[:len(l) // 2]) if n < l[len(l) // 2]
                      else (-1 if chop(n, l[len(l) // 2:]) == -1
                            else len(l) // 2 + chop(n, l[len(l) // 2:])))))
