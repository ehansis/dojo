import itertools

from . import klondike


def test_get_deck():
    d = klondike.get_deck()
    assert len(d) == 52
    assert len(set([str(c) for c in d])) == 52
    for s in klondike.Suite:
        for v in range(1, 13 + 1):
            assert klondike.Card(suite=s, value=v) in d


def test_deal():
    g = klondike.deal()

    assert len(g.foundation) == 4
    for f in g.foundation:
        assert len(f) == 0

    assert len(g.discard) == 0

    assert len(g.tableaus) == 7
    for i, t in enumerate(g.tableaus):
        assert len(t) == i + 1

    assert len(g.stock) == 52 - 28

    full_deck = itertools.chain(g.stock, *g.tableaus)
    assert sorted(full_deck) == sorted(klondike.get_deck())
