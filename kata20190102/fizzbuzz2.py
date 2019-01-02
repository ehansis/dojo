"""Fizzbuzz 2 with dict lookups"""

fizzes = {3 * i: 'Fizz' for i in range(1, 100 // 3 + 1)}
buzzes = {5 * i: 'Buzz' for i in range(1, 100 // 5 + 1)}
fizzes_buzzes = {i: fizzes.get(i, '') + buzzes.get(i, '') for i in set(fizzes.keys()).union(buzzes.keys())}


def go():
    out = [fizzes_buzzes.get(i, str(i)) for i in range(1, 101)]
    return out
