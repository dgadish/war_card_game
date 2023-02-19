"""
Deck class which should instantiate with a full deck of cards that can be shuffled
"""

from random import shuffle

from wargame.objects.card import Card
from wargame.objects.constants import RANKS, SUITS


class Deck:
    """Represents a standard deck of 52 playing cards.

    Attributes:
        all_cards (list[Card]): list of all cards within the deck
    """

    def __init__(self) -> None:
        self.all_cards = []

        for suit in SUITS:
            for rank in RANKS:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        """randomly shuffle the deck of cards. Shuffle done in place"""
        shuffle(self.all_cards)

    def deal_one(self) -> Card:
        """deal a card from the deck, returning it and removing it from the deck"""
        return self.all_cards.pop()
