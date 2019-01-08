import typing

def go():
    numbers = range(1, 101)
    is_fizz = set(range(3, 101, 3))
    is_buzz = set(range(5, 101, 5))
    is_number = set(range(1, 101)).difference(is_fizz).difference(is_buzz)
    str_numbers = {i: str(i) for i in numbers}  # type: typing.Dict[int, str]
    return [str_numbers[n] * (n in is_number)
            + 'Fizz' * (n in is_fizz)
            + 'Buzz' * (n in is_buzz)
            for n in numbers]
