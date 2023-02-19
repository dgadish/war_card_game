"""
Test the Deck class
"""

from wargame.objects.card import Card
from wargame.objects.deck import Deck


def test_deck_instansiation() -> None:
    """Check that the deck is instansiated with the correct number of cards.
    Check that the cards are of the Card type"""
    deck = Deck()

    assert len(deck.all_cards) == 52
    for card in deck.all_cards:
        assert type(card) == Card
