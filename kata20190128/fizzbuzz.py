def fizzbuzz(n):
    numbers = range(1, n + 1)
    out = [str(i) for i in numbers]

    for i in numbers:
        if i % 15 == 0:
            out[i - 1] = 'fizzbuzz'
        elif i % 5 == 0:
            out[i - 1] = 'buzz'
        elif i % 3 == 0:
            out[i - 1] = 'fizz'

    return out
