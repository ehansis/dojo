from typing import Dict, List, Tuple
import enum
import itertools
import random

import attr


#
# Types
#

class Suite(enum.IntEnum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4


class Color(enum.Enum):
    RED = 1
    BLACK = 2


SUITE_TO_COLOR: Dict[Suite, Color] = {
    Suite.HEARTS: Color.RED,
    Suite.DIAMONDS: Color.RED,
    Suite.CLUBS: Color.BLACK,
    Suite.SPADES: Color.BLACK
}


@attr.s
class Card:
    suite: Suite = attr.ib()
    value: int = attr.ib()  # value, 1...13, 1 = Ace, 13 = King
    color: Color = attr.ib(default=attr.Factory(lambda obj: SUITE_TO_COLOR[obj.suite], takes_self=True))


Pile = List[Card]  # index 0 = top card


@attr.s
class Game:
    stock: Pile = attr.ib()
    tableaus: Tuple[Pile] = attr.ib()

    # Caution! Setting [] or as default directly will cause default to be mutable! Use a factory instead.
    discard: Pile = attr.ib(default=attr.Factory(lambda: []))
    foundations: Tuple[Pile] = attr.ib(default=attr.Factory(lambda: ([], [], [], [])))


class MoveType(enum.Enum):
    DISCARD_TO_STOCK = 1
    STOCK_TO_DISCARD = 2
    TABLEAU_TO_FOUNDATION = 3
    TABLEAU_TO_TABLEAU = 4
    DISCARD_TO_FOUNDATION = 5
    DISCARD_TO_TABLEAU = 6


@attr.s
class Move:
    move_type: MoveType = attr.ib()
    from_pile: Pile = attr.ib()
    to_pile: Pile = attr.ib()
    n: int = attr.ib()
    new_exposed_card: bool = attr.ib()
    leaves_from_empty: bool = attr.ib()


#
# Dealer
#

def get_deck() -> Pile:
    """Get a full (sorted) deck of cards"""
    # noinspection PyTypeChecker
    return [Card(suite=s, value=v) for s, v in itertools.product(Suite, range(1, 13 + 1))]


def deal(seed: int or None = None) -> Game:
    """Deal a new game

    Args:
        seed: optional random seed
    """
    if seed is not None:
        random.seed(seed)

    deck = get_deck()
    random.shuffle(deck)
    i: int = 0

    tableaus: List[Pile] = []
    for n in range(1, 7 + 1):
        tableaus.append(deck[i: i + n])
        i += n

    return Game(stock=deck[i:], tableaus=tuple(tableaus))


#
# Check possible moves
#

def check_discard_to_stock(game: Game) -> List[Move]:
    """Check if turning the discard pile over to make the new stock is possible

    Args:
        game: the game

    Returns:
        list of one move or empty list if not possible
    """
    if len(game.stock) == 0:
        return [Move(
            move_type=MoveType.DISCARD_TO_STOCK,
            from_pile=game.discard,
            to_pile=game.stock,
            n=len(game.discard),
            new_exposed_card=True,
            leaves_from_empty=True
        )]
    else:
        return []


def check_stock_to_discard(game: Game) -> List[Move]:
    """Check if we can turn over the top card of the stock to the discard pile

    Args:
        game: the game

    Returns:
        list of one move or empty list if not possible
    """
    if len(game.stock) > 0:
        return [Move(
            move_type=MoveType.STOCK_TO_DISCARD,
            from_pile=game.stock,
            to_pile=game.discard,
            n=1,
            new_exposed_card=True,
            leaves_from_empty=len(game.stock) == 1
        )]
    else:
        return []


def _check_fits_foundation(card: Card, foundation: Pile) -> bool:
    """Check if a given card fits onto a given foundation"""
    if len(foundation) == 0 and card.value == 1:
        return True
    elif len(foundation) > 0 and card.value == foundation[0].value + 1 and card.suite == foundation[0].suite:
        return True
    else:
        return False


def _moves_to_foundation(from_pile: Pile, game: Game) -> List[Move]:
    """Check for moves onto a given foundation"""

    if len(from_pile) == 0:
        return []

    moves = []
    for foundation in game.foundations:
        if _check_fits_foundation(from_pile[0], foundation):
            moves.append(Move(
                move_type=MoveType.TABLEAU_TO_FOUNDATION,
                from_pile=from_pile,
                to_pile=foundation,
                n=1,
                new_exposed_card=len(from_pile) > 1,
                leaves_from_empty=len(from_pile) == 1
            ))

    return moves


def check_tableau_to_foundation(game: Game) -> List[Move]:
    """Check for moves that move a card from a tableau pile to a foundation pile

    Args:
        game: the game

    Returns:
        list of possible moves
    """
    moves = []
    for tableau in game.tableaus:
        moves += _moves_to_foundation(tableau, game)

    return moves


def check_discard_to_foundation(game: Game) -> List[Move]:
    """Check for moves that move a card from a discard pile to a foundation pile

    Args:
        game: the game

    Returns:
        list of possible moves
    """
    return _moves_to_foundation(game.discard, game)

