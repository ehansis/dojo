def fizzbuzz(n):
    num = range(1, n + 1)
    numbers = [str(i) if i % 3 != 0 and i % 5 != 0 else '' for i in num]
    fizzes = ["fizz" if i % 3 == 0 else '' for i in num]
    buzzes = ["buzz" if i % 5 == 0 else '' for i in num]

    return [''.join(c) for c in zip(numbers, fizzes, buzzes)]
