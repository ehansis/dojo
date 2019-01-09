from kata20190109.chop import chop


class TestChop:

    def test_tdd(self):
        assert -1 == chop(5, [])
        assert -1 == chop(5, [3])
        assert 0 == chop(5, [5])
        assert 1 == chop(5, [1, 5])
        assert 0 == chop(1, [1, 5])
        assert 2 == chop(5, [1, 2, 5, 6])
        assert 3 == chop(6, [1, 2, 5, 6])

    def test_acceptance(self):
        # http://codekata.com/kata/kata02-karate-chop/

        assert -1 == chop(3, [])
        assert -1 == chop(3, [1])
        assert 0 == chop(1, [1])

        assert 0 == chop(1, [1, 3, 5])
        assert 1 == chop(3, [1, 3, 5])
        assert 2 == chop(5, [1, 3, 5])
        assert -1 == chop(0, [1, 3, 5])
        assert -1 == chop(2, [1, 3, 5])
        assert -1 == chop(4, [1, 3, 5])
        assert -1 == chop(6, [1, 3, 5])

        assert 0 == chop(1, [1, 3, 5, 7])
        assert 1 == chop(3, [1, 3, 5, 7])
        assert 2 == chop(5, [1, 3, 5, 7])
        assert 3 == chop(7, [1, 3, 5, 7])
        assert -1 == chop(0, [1, 3, 5, 7])
        assert -1 == chop(2, [1, 3, 5, 7])
        assert -1 == chop(4, [1, 3, 5, 7])
        assert -1 == chop(6, [1, 3, 5, 7])
        assert -1 == chop(8, [1, 3, 5, 7])
