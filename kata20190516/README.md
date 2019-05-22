Klondike kata, v1
=================

Design ideas
------------

**Functional style**: One central representation of the game state gets passed around (nested `attrs` classes).
Various other `attrs` classes may exist to represent other parts of the game, like possible moves.

**Typed**: Use type hints throughout.

*Dealer*: Initializes a game state to a new, random game (with optional fixed random seed).

*Inspector*: Finds possible valid moves, checks if the game is won (or lost).
Subroutines to check validity of different moves for specific cards and game states.
    - If stock pile is empty, return turning it over to make it the new stock as only move

*Chooser*: Chooses one move amongst the valid ones returned by the inspector. 
Different game strategies are implemented as separate player functions, one of which is assigned to be the
active player in the main game loop.

*Executor*: Executes the chosen move

*Main game loop*: Initialization, then simple loop over inspector and player. Only the player has multiple flavors.


State/data classes
------------------

*Card*: 
- Suite: constants HEART, DIAMOND, CLUBS, SPADE
- Color: constants RED, BLACK
- Value: 1 ... 13 (1 = Ace)

*Pile*:
- List of cards, first = top

*Game*:
- Stock: pile
- Discard: pile
- Tableaus: list of 7 piles
- Foundation: list of 4 piles

*Move*:
- Type: constant, one of 
    * DISCARD_TO_STOCK (turn it over)
    * STOCK_TO_DISCARD (one card)
    * TABLEAU_TO_FOUNDATION (one card)
    * DISCARD_TO_FOUNDATION (one card)
    * DISCARD_TO_TABLEAU (one card)
    * TABLEAU_TO_TABLEAU (one or several cards)
- From: from pile
- To: to pile
- N: Number of cards moved
- New: True if the move leaves a new card exposed to be turned over, false otherwise
- Empty: True if the move leaves the from-pile empty



