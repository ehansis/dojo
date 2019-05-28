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

    assert len(g.foundations) == 4
    for f in g.foundations:
        assert len(f) == 0

    assert len(g.discard) == 0

    assert len(g.tableaus) == 7
    for i, t in enumerate(g.tableaus):
        assert len(t) == i + 1

    assert len(g.stock) == 52 - 28

    full_deck = itertools.chain(g.stock, *g.tableaus)
    assert sorted(full_deck) == sorted(klondike.get_deck())


def test_check_discard_to_stock():
    g = klondike.deal()
    assert len(klondike.check_discard_to_stock(g)) == 0

    g = klondike.deal()
    g.discard = g.tableaus[6]
    g.stock = []
    assert klondike.check_discard_to_stock(g) == [
        klondike.Move(
            move_type=klondike.MoveType.DISCARD_TO_STOCK,
            from_pile=g.discard,
            to_pile=g.stock,
            n=7,
            new_exposed_card=True,
            leaves_from_empty=True
        )]


def test_check_stock_do_discard():
    g = klondike.deal()
    g.stock, g.discard = g.discard, g.stock
    assert len(klondike.check_stock_to_discard(g)) == 0

    g = klondike.deal()
    assert klondike.check_stock_to_discard(g) == [
        klondike.Move(
            move_type=klondike.MoveType.STOCK_TO_DISCARD,
            from_pile=g.stock,
            to_pile=g.discard,
            n=1,
            new_exposed_card=True,
            leaves_from_empty=False
        )]

    g = klondike.deal()
    g.stock = g.stock[:1]
    assert klondike.check_stock_to_discard(g) == [
        klondike.Move(
            move_type=klondike.MoveType.STOCK_TO_DISCARD,
            from_pile=g.stock,
            to_pile=g.discard,
            n=1,
            new_exposed_card=True,
            leaves_from_empty=True
        )]


def test_check_tableau_to_foundation():
    g = klondike.deal()
    for t in g.tableaus:
        t[0] = klondike.Card(suite=klondike.Suite.HEARTS, value=2)
    assert len(klondike.check_tableau_to_foundation(g)) == 0

    g = klondike.deal()
    for t in g.tableaus:
        t[0] = klondike.Card(suite=klondike.Suite.HEARTS, value=1)
    moves = klondike.check_tableau_to_foundation(g)
    assert len(moves) == 28
    assert moves[0] == klondike.Move(
        move_type=klondike.MoveType.TABLEAU_TO_FOUNDATION,
        from_pile=g.tableaus[0],
        to_pile=g.foundations[0],
        n=1,
        new_exposed_card=False,
        leaves_from_empty=True)
    assert moves[1] == klondike.Move(
        move_type=klondike.MoveType.TABLEAU_TO_FOUNDATION,
        from_pile=g.tableaus[0],
        to_pile=g.foundations[1],
        n=1,
        new_exposed_card=False,
        leaves_from_empty=True)
    assert moves[-1] == klondike.Move(
        move_type=klondike.MoveType.TABLEAU_TO_FOUNDATION,
        from_pile=g.tableaus[6],
        to_pile=g.foundations[3],
        n=1,
        new_exposed_card=True,
        leaves_from_empty=False)

    g = klondike.deal()
    for i, t in enumerate(g.tableaus):
        t[0] = klondike.Card(suite=klondike.Suite.HEARTS, value=i + 1)
    for f in g.foundations[:-1]:
        f.append(klondike.Card(suite=klondike.Suite.DIAMONDS, value=3))
    g.foundations[-1].append(klondike.Card(suite=klondike.Suite.HEARTS, value=3))
    moves = klondike.check_tableau_to_foundation(g)
    assert len(moves) == 1
    assert moves[0] == klondike.Move(
        move_type=klondike.MoveType.TABLEAU_TO_FOUNDATION,
        from_pile=g.tableaus[3],
        to_pile=g.foundations[3],
        n=1,
        new_exposed_card=True,
        leaves_from_empty=False)


def test_check_discard_to_foundation():
    g = klondike.deal()
    g.discard.append(klondike.Card(suite=klondike.Suite.HEARTS, value=2))
    assert len(klondike.check_discard_to_foundation(g)) == 0

    g = klondike.deal()
    g.discard.append(klondike.Card(suite=klondike.Suite.HEARTS, value=1))
    g.discard.append(klondike.Card(suite=klondike.Suite.HEARTS, value=2))
    moves = klondike.check_discard_to_foundation(g)
    assert len(moves) == 4
    assert moves[0] == klondike.Move(
        move_type=klondike.MoveType.DISCARD_TO_FOUNDATION,
        from_pile=g.discard,
        to_pile=g.foundations[0],
        n=1,
        new_exposed_card=True,
        leaves_from_empty=False)
    assert moves[-1] == klondike.Move(
        move_type=klondike.MoveType.DISCARD_TO_FOUNDATION,
        from_pile=g.discard,
        to_pile=g.foundations[3],
        n=1,
        new_exposed_card=True,
        leaves_from_empty=False)

    g = klondike.deal()
    g.discard.append(klondike.Card(suite=klondike.Suite.DIAMONDS, value=3))
    for i, f in enumerate(g.foundations[:-1]):
        f.append(klondike.Card(suite=klondike.Suite.DIAMONDS, value=i + 1))
    g.foundations[-1].append(klondike.Card(suite=klondike.Suite.HEARTS, value=2))
    moves = klondike.check_discard_to_foundation(g)
    assert len(moves) == 1
    assert moves[0] == klondike.Move(
        move_type=klondike.MoveType.DISCARD_TO_FOUNDATION,
        from_pile=g.discard,
        to_pile=g.foundations[1],
        n=1,
        new_exposed_card=False,
        leaves_from_empty=True)


