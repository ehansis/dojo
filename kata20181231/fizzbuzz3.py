# fizzbuzz v3, functional style


def append(l):
    v = len(l) + 1
    if v % 3 == 0:
        if v % 5 == 0:
            w = "FizzBuzz"
        else:
            w = "Fizz"
    elif v % 5 == 0:
        w = "Buzz"
    else:
        w = v

    return l + [w]


def go():
    out = []
    while len(out) < 100:
        out = append(out)

    return out
