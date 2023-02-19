"""
Test the Deck class
"""

from wargame.objects.card import Card
from wargame.objects.constants import RANKS, SUITS
from wargame.objects.deck import Deck


def test_deck_instansiation() -> None:
    """Check that the deck is instansiated with the correct number of cards.
    Check that the cards are of the Card type"""
    deck = Deck()

    assert len(deck.all_cards) == 52
    for card in deck.all_cards:
        assert type(card) == Card


def test_deck_shuffle() -> None:
    """Ensure that the deck is randomly shuffled"""

    unshuffled_list = []
    for suit in SUITS:
        for rank in RANKS:
            unshuffled_list.append(Card(suit, rank))

    deck = Deck()
    deck.shuffle()

    assert deck.all_cards != unshuffled_list


def test_deck_deal_one() -> None:
    """Check that a card is returned and removed from the deck"""

    deck = Deck()
    card = deck.deal_one()

    assert type(card) == Card
    assert len(deck.all_cards) == 51
