"""
Test the player class
"""

from wargame.objects.card import Card
from wargame.objects.player import Player

TEST_NAME = "test_name"
TEST_CARD = Card("hearts", "two")
TEST_CARDS = [TEST_CARD, Card("diamonds", "three"), Card("clubs", "ace")]


def test_player_description():
    """Test the player class string value"""
    player = Player(TEST_NAME)
    assert str(player) == f"Player: {TEST_NAME}\nNumber of Cards: 0"


def test_player_add_cards():
    """Test that cards are added to the player deck"""
    player = Player(TEST_NAME)
    player.add_cards([TEST_CARD])
    assert player.all_cards == [TEST_CARD]
    assert len(player.all_cards) == 1


def test_player_remove_one():
    """Test that cards are correctly removed from the top player deck"""
    player = Player(TEST_NAME)
    player.add_cards(TEST_CARDS)
    removed_card = player.remove_card()
    assert removed_card == TEST_CARD
    assert len(player.all_cards) == 2
