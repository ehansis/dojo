# FizzBuzz kata, http://codingdojo.org/kata/FizzBuzz/


def go():
    out = list(range(101))

    for i in range(100 // 3 + 1):
        out[i * 3] = "Fizz"

    for i in range(100 // 5 + 1):
        if (i * 5) % 3 == 0:
            out[i * 5] = "FizzBuzz"
        else:
            out[i * 5] = "Buzz"

    return out[1:]
