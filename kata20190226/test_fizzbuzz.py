from . import fizzbuzz


class TestFizzBuzz:

    def test_tdd(self):
        s = fizzbuzz.f(1)
        assert s == ['1']

        s = fizzbuzz.f(3)
        assert s == ['1', '2', 'fizz']

        s = fizzbuzz.f(5)
        assert s == ['1', '2', 'fizz', '4', 'buzz']

        s = fizzbuzz.f(15)
        assert s == ['1', '2', 'fizz', '4', 'buzz',
                     'fizz', '7', '8', 'fizz', 'buzz',
                     '11', 'fizz', '13', '14', 'fizzbuzz']

        s = fizzbuzz.f(30)
        assert s == ['1', '2', 'fizz', '4', 'buzz',
                     'fizz', '7', '8', 'fizz', 'buzz',
                     '11', 'fizz', '13', '14', 'fizzbuzz',
                     '16', '17', 'fizz', '19', 'buzz',
                     'fizz', '22', '23', 'fizz', 'buzz',
                     '26', 'fizz', '28', '29', 'fizzbuzz']
