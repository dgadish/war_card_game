"""
Tests for the Card class
"""

import pytest

import wargame.objects.constants as constants
from wargame.objects.card import Card


@pytest.mark.parametrize(
    "input_suit, input_rank, expected_value",
    [
        ("hearts", "Five", 5),
        ("Clubs", "Ace", 14),
        ("spades", "jack", 11),
        ("Diamonds", "four", 4),
    ],
)
def test_card_value(input_suit: str, input_rank: str, expected_value: int) -> None:
    """Test that the card is instansiated with the correct values"""

    card = Card(suit=input_suit, rank=input_rank)
    assert card.rank == input_rank.lower()
    assert card.suit == input_suit.lower()
    assert card.value == expected_value


@pytest.mark.parametrize(
    "input_suit, input_rank, expected_error_string",
    [
        ("Herts", "five", constants.SUIT_ERROR),
        ("Clubs", "twelve", constants.RANK_ERROR),
    ],
)
def test_card_errors(
    input_suit: str,
    input_rank: str,
    expected_error_string: str,
) -> None:
    """Test that the correct errors are thrown if instantiated incorrectly"""

    with pytest.raises(ValueError, match=expected_error_string):
        Card(suit=input_suit, rank=input_rank)


def test_card_print() -> None:
    """Test that the correct print statement is returned"""

    card = Card("hearts", "king")
    assert str(card) == "King of Hearts"


def test_card_comparison_operations() -> None:
    """Test that the operators behave as expected"""

    two_hearts = Card("hearts", "two")
    two_clubs = Card("clubs", "two")
    ace_hearts = Card("hearts", "ace")

    assert two_hearts == two_clubs
    assert not (two_hearts == ace_hearts)
    assert not (two_clubs == ace_hearts)
    assert not (two_hearts != two_clubs)
    assert two_hearts != ace_hearts
    assert two_clubs != ace_hearts
    assert two_hearts >= two_clubs
    assert not (two_hearts >= ace_hearts)
    assert not (two_clubs >= ace_hearts)
    assert two_hearts <= two_clubs
    assert two_hearts <= ace_hearts
    assert two_clubs <= ace_hearts
    assert not (two_hearts > two_clubs)
    assert not (two_hearts > ace_hearts)
    assert not (two_clubs > ace_hearts)
    assert not (two_hearts < two_clubs)
    assert two_hearts < ace_hearts
    assert two_clubs < ace_hearts
