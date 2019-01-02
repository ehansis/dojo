"""Fizzbuzz standard implementation"""


def go():
    out = [str(i + 1) for i in range(100)]

    for i in range(100):
        if (i + 1) % 3 == 0:
            out[i] = 'Fizz'
        if (i + 1) % 5 == 0:
            out[i] = 'Buzz'
        if (i + 1) % 15 == 0:
            out[i] = 'FizzBuzz'

    return out
