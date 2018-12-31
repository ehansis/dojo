from kata20181231 import fizzbuzz


class TestFizzBuzz:

    def test_fizzbuzz(self):
        output = fizzbuzz.go()

        assert output[0] == 1
        assert output[1] == 2
        assert output[2] == "Fizz"
        assert output[3] == 4
        assert output[4] == "Buzz"
        assert output[14] == "FizzBuzz"

    def test_acceptance(self):
        output = fizzbuzz.go()

        for i in range(1, 101):
            if i % 3 == 0:
                if i % 5 == 0:
                    assert output[i - 1] == "FizzBuzz"
                else:
                    assert output[i - 1] == "Fizz"
            elif i % 5 == 0:
                assert output[i - 1] == "Buzz"
