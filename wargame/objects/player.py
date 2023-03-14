"""Player class for hadnling the cards in a players deck"""

from wargame.objects.card import Card


class Player:
    """Represents a game player with a name and deck of cards

    Attributes:
        name (str): Player name

    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.all_cards: list[Card] = []

    def __str__(self) -> str:
        return f"Player: {self.name}\nNumber of Cards: {len(self.all_cards)}"

    def remove_card(self) -> Card:
        """Remove the top card from the players card list"""
        return self.all_cards.pop(0)

    def add_cards(self, new_cards: list[Card]) -> None:
        """Add cards to the bottom of the players card set"""
        self.all_cards.extend(new_cards)
