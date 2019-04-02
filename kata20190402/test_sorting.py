import random

from . import sorting


class TestRack:

    def test_tdd(self):
        rack = sorting.Rack()

        assert [] == rack.balls()
        rack.add(20)
        assert [20] == rack.balls()
        rack.add(10)
        assert [10, 20] == rack.balls()
        rack.add(30)
        assert [10, 20, 30] == rack.balls()

    def test_random(self):
        random.seed(1324)
        for _ in range(100):
            n_max = random.randint(1, 100)
            rack = sorting.Rack(n_max=n_max)

            n = random.randint(1, n_max)
            ref = set()
            for _ in range(n):
                i = random.randrange(0, n_max)
                ref.add(i)
                rack.add(i)

                assert rack.balls() == sorted(ref)


class TestCharCount:

    def test_tdd(self):
        assert "" == sorting.char_count("")
        assert "aaabbbccc" == sorting.char_count("AbcbCaCBA")

        assert "aaaaabbbbcccdeeeeeghhhiiiiklllllllmnnnnooopprsssstttuuvwyyyy" == sorting.char_count(
            "When not studying nuclear physics, Bambi likes to play beach volleyball.")
