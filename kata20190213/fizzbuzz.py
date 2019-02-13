from itertools import cycle


def fizzbuzz(n):
    out = (str(i) for i in range(1, n + 1))
    fizzes = cycle([""] * 2 + ['fizz'])
    buzzes = cycle([""] * 4 + ['buzz'])
    fizzbuzzes = cycle([""] * 14 + ['fizzbuzz'])

    for lst in [fizzes, buzzes, fizzbuzzes]:
        out = [w if len(l) == 0 else l for w, l in zip(out, lst)]

    return out
