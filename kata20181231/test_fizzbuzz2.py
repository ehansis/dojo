from kata20181231 import fizzbuzz2


class TestGo:

    def test_tdd(self):
        out = fizzbuzz2.go()

        for i, v in enumerate(out):
            if (i + 1) % 3 == 0 or '3' in str(i + 1):
                if (i + 1) % 5 == 0 or '5' in str(i + 1):
                    assert v == 'FizzBuzz'
                else:
                    assert v == 'Fizz'
            elif (i + 1) % 5 == 0 or '5' in str(i + 1):
                assert v == 'Buzz'
            else:
                assert v == i + 1
