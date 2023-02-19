"""
Card class which should cover suit, rank and value
"""

import wargame.objects.constants as constants


class Suit:
    """Suit class to ensure valid suit when Card class is instantiate"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not value.lower() in constants.SUITS:
            raise ValueError(constants.SUIT_ERROR)
        # pylint warning caused by self.value being
        # set outside of __init__ block to be ignored
        self.value = value  # pylint: disable=attribute-defined-outside-init


class Rank:
    """Rank class to ensure valid suit when Card class is instantiate"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not value.lower() in constants.RANKS:
            raise ValueError(constants.RANK_ERROR)
        # pylint warning caused by self.value being
        # set outside of __init__ block to be ignored
        self.value = value  # pylint: disable=attribute-defined-outside-init


class Card:
    """A standard playing card with suit and rank

    Attributes:
        suit (str): Must be one of {"hearts", "diamonds", "spades", "clubs"}
        rank (str): Must be one of {
                                        "two",
                                        "three",
                                        "four",
                                        "five",
                                        "six",
                                        "seven",
                                        "eight",
                                        "nine",
                                        "ten",
                                        "jack",
                                        "queen",
                                        "king",
                                        "ace"
                                    }
    """

    suit = Suit()
    rank = Rank()

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit.lower()
        self.rank = rank.lower()
        # Set numeric value to allow for comparison of different cards
        self.value = constants.VALUE_DICT[rank.lower()]

    def __str__(self) -> str:
        return self.rank.capitalize() + " of " + self.suit.capitalize()

    def __eq__(self, __o) -> bool:
        return self.value == __o.value

    def __ne__(self, __o) -> bool:
        return self.value != __o.value

    def __ge__(self, __o) -> bool:
        return self.value >= __o.value

    def __gt__(self, __o) -> bool:
        return self.value > __o.value

    def __le__(self, __o) -> bool:
        return self.value <= __o.value

    def __lt__(self, __o) -> bool:
        return self.value < __o.value
