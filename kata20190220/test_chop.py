from . import chop


class TestChop:

    def test_acceptance(self):
        # http://codekata.com/kata/kata02-karate-chop.c/

        assert -1 == chop.c(3, [])
        assert -1 == chop.c(3, [1])
        assert 0 == chop.c(1, [1])

        assert 0 == chop.c(1, [1, 3, 5])
        assert 1 == chop.c(3, [1, 3, 5])
        assert 2 == chop.c(5, [1, 3, 5])
        assert -1 == chop.c(0, [1, 3, 5])
        assert -1 == chop.c(2, [1, 3, 5])
        assert -1 == chop.c(4, [1, 3, 5])
        assert -1 == chop.c(6, [1, 3, 5])

        assert 0 == chop.c(1, [1, 3, 5, 7])
        assert 1 == chop.c(3, [1, 3, 5, 7])
        assert 2 == chop.c(5, [1, 3, 5, 7])
        assert 3 == chop.c(7, [1, 3, 5, 7])
        assert -1 == chop.c(0, [1, 3, 5, 7])
        assert -1 == chop.c(2, [1, 3, 5, 7])
        assert -1 == chop.c(4, [1, 3, 5, 7])
        assert -1 == chop.c(6, [1, 3, 5, 7])
        assert -1 == chop.c(8, [1, 3, 5, 7])
