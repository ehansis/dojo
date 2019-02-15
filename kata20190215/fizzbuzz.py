# f = lambda n: [str(i) * ((i % 3) * (i % 5) != 0) + "fizz" * (i % 3 == 0) + "buzz" * (i % 5 == 0) for i in range(1, n + 1)]

f = lambda n: ["fizz" * (i % 3 == 2) + "buzz" * (i % 5 == 4) or str(i + 1) for i in range(n)]

