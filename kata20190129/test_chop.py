from . import chop


class TestChop:

    def test_chop(self):
        assert -1 == chop.chop(3, [])
        assert 0 == chop.chop(3, [3])
        assert -1 == chop.chop(3, [5])
        assert 1 == chop.chop(5, [1, 5])

    def test_acceptance(self):
        # http://codekata.com/kata/kata02-karate-chop.chop/

        assert -1 == chop.chop(3, [])
        assert -1 == chop.chop(3, [1])
        assert 0 == chop.chop(1, [1])

        assert 0 == chop.chop(1, [1, 3, 5])
        assert 1 == chop.chop(3, [1, 3, 5])
        assert 2 == chop.chop(5, [1, 3, 5])
        assert -1 == chop.chop(0, [1, 3, 5])
        assert -1 == chop.chop(2, [1, 3, 5])
        assert -1 == chop.chop(4, [1, 3, 5])
        assert -1 == chop.chop(6, [1, 3, 5])

        assert 0 == chop.chop(1, [1, 3, 5, 7])
        assert 1 == chop.chop(3, [1, 3, 5, 7])
        assert 2 == chop.chop(5, [1, 3, 5, 7])
        assert 3 == chop.chop(7, [1, 3, 5, 7])
        assert -1 == chop.chop(0, [1, 3, 5, 7])
        assert -1 == chop.chop(2, [1, 3, 5, 7])
        assert -1 == chop.chop(4, [1, 3, 5, 7])
        assert -1 == chop.chop(6, [1, 3, 5, 7])
        assert -1 == chop.chop(8, [1, 3, 5, 7])
