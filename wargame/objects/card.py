"""
Card class which should cover suit, rank and value
"""

import wargame.objects.constants as constants


class Suit:
    """Suit class to ensure valid suit when Card class is initiated"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not value.lower() in constants.SUITS:
            raise ValueError(constants.SUIT_ERROR)
        # pylint warning caused by self.value being
        # set outside of __init__ block to be ignored
        self.value = value  # pylint: disable=attribute-defined-outside-init


class Rank:
    """Rank class to ensure valid suit when Card class is initiated"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not value.lower() in constants.RANKS:
            raise ValueError(constants.RANK_ERROR)
        # pylint warning caused by self.value being
        # set outside of __init__ block to be ignored
        self.value = value  # pylint: disable=attribute-defined-outside-init


class Card:
    """Class that represents a playing card"""

    suit = Suit()
    rank = Rank()

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit.lower()
        self.rank = rank.lower()
        self.value = constants.VALUE_DICT[rank.lower()]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit
