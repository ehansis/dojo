def get_cols():
    with open('weather.dat') as f:
        first_line = f.readline().rstrip()

    col_names = first_line.split()
    indices = [first_line.index(c) for c in col_names]
    start = [0] + [indices[i] + len(col_names[i]) for i in range(len(col_names) - 1)]
    end = start[1:] + [len(first_line)]
    num = [e - s for s, e in zip(start, end)]
    return {c: s for c, s in zip(col_names, start)}, {c: n for c, n in zip(col_names, num)}

