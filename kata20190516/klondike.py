from typing import Dict, List, Tuple
import enum
import itertools
import random

import attr


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
    value: int = attr.ib()  # value, 1...13
    color: Color = attr.ib(default=attr.Factory(lambda obj: SUITE_TO_COLOR[obj.suite], takes_self=True))


@attr.s
class Game:
    stock: List[Card] = attr.ib()
    tableaus: Tuple[List[Card]] = attr.ib()
    discard: List[Card] = attr.ib(default=[])
    foundation: Tuple[List[Card]] = attr.ib(default=([], [], [], []))


def get_deck() -> List[Card]:
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

    tableaus: List[List[Card]] = []
    for n in range(1, 7 + 1):
        tableaus.append(deck[i: i + n])
        i += n

    return Game(stock=deck[i:], tableaus=tuple(tableaus))
