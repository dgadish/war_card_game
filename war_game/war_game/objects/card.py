"""
Card class which should cover suit, rank and value
"""


class Card:
    """Class that represents a playing card"""

    def __init__(self, suit: str, rank: int) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return self.rank + " of " + self.suit
