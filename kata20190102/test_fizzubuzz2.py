from kata20190102 import fizzbuzz2


class TestFizzBuzz:

    def test_dicts(self):

        assert len(fizzbuzz2.fizzes) == 33
        assert len(fizzbuzz2.buzzes) == 20
        assert len(fizzbuzz2.fizzes_buzzes) == 100

    def test_acceptane(self):

        out = fizzbuzz2.go()

        for i, v in enumerate(out):
            if (i + 1) % 3 == 0:
                if (i + 1) % 5 == 0:
                    assert v == 'FizzBuzz'
                else:
                    assert v == 'Fizz'
            elif (i + 1) % 5 == 0:
                assert v == 'Buzz'
            else:
                assert v == str(i + 1)
