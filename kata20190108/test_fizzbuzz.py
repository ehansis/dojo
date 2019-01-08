from kata20190108 import fizzbuzz

class TestFizzBuzz:

    def test_simple(self):
        out = fizzbuzz.go()

        assert out[0] == '1'
        assert out[1] == '2'
        assert out[2] == 'Fizz'
        assert out[3] == '4'
        assert out[4] == 'Buzz'
        assert out[5] == 'Fizz'
        assert out[13] == '14'
        assert out[14] == 'FizzBuzz'
