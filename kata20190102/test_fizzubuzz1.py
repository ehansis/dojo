from kata20190102 import fizzbuzz1


class TestFizzBuzz:

    def test_values(self):

        out = fizzbuzz1.go()
        assert len(out) == 100

        assert out[0] == '1'
        assert out[1] == '2'
        assert out[2] == 'Fizz'
        assert out[3] == '4'
        assert out[4] == 'Buzz'
        assert out[14] == 'FizzBuzz'

    def test_acceptane(self):

        out = fizzbuzz1.go()

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
