"""
Card class which should cover suit, rank and value
"""

value_dict = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 11,
    "queen": 12,
    "king": 13,
    "ace": 14
}

suits = ("hearts", "diamonds", "spades", "clubs")

ranks = set(value_dict.keys())


class Suit:
    """Suit class to ensure valid suit when Card class is initiated"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")

        if not value.lower() in suits:
            raise ValueError("Must be a valid suit")
        # pylint warning caused by self.value being set outside of __init__ block to be ignored
        self.value = value  # pylint: disable=attribute-defined-outside-init


class Rank:
    """Suit class to ensure valid suit when Card class is initiated"""

    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")

        if not value.lower() in ranks:
            raise ValueError("Must be a valid rank")
        # pylint warning caused by self.value being set outside of __init__ block to be ignored
        self.value = value  # pylint: disable=attribute-defined-outside-init


class Card:
    """Class that represents a playing card"""

    suit = Suit()
    rank = Rank()

    def __init__(self, suit: str, rank: int) -> None:
        self.suit = suit.lower()
        self.rank = rank.lower()
        self.value = value_dict[rank.lower()]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit
