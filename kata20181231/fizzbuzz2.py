# Fizzbuzz kata, v2


def go():
    out = []
    for i in range(1, 101):
        if i % 3 == 0 or '3' in str(i):
            if i % 5 == 0 or '5' in str(i):
                out.append("FizzBuzz")
            else:
                out.append("Fizz")
        elif i % 5 == 0 or '5' in str(i):
            out.append("Buzz")
        else:
            out.append(i)

    return out
