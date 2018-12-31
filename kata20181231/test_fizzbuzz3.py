from kata20181231 import fizzbuzz3


class TestFizzBuzz:

    def test_acceptance(self):
        output = fizzbuzz3.go()

        for i in range(1, 101):
            if i % 3 == 0:
                if i % 5 == 0:
                    assert output[i - 1] == "FizzBuzz"
                else:
                    assert output[i - 1] == "Fizz"
            elif i % 5 == 0:
                assert output[i - 1] == "Buzz"
