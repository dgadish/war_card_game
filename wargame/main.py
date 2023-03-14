"""Script for the logic to run the game"""

from wargame.objects.player import Player
from wargame.objects.deck import Deck
from wargame.objects.card import Card

# game set up
# instantiate the players
player_one = Player("One")
player_two = Player("Two")

# instantiate and shuffle the deck
deck = Deck()
deck.shuffle()

# deal cards to the players
while len(deck.all_cards) != 0:
    player_one.add_cards([deck.deal_one()])
    player_two.add_cards([deck.deal_one()])

# game logic
game_on = True
round_num = 0

while game_on:
    # check for end of game
    if len(player_one.all_cards) == 0:
        print("Player One is out of cards! Player Two wins!")
        print(f"Rounds played: {round_num}")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards! Player One wins!")
        print(f"Rounds played: {round_num}")
        game_on = False
        break

    round_num += 1
    print(f"Round {round_num}")

    player_one_hand: list[Card] = []
    player_two_hand: list[Card] = []

    player_one_hand.append(player_one.remove_card())
    player_two_hand.append(player_two.remove_card())

    at_war = True

    # start card comparison
    while at_war:
        if player_one_hand[-1] > player_two_hand[-1]:
            player_one.add_cards(player_one_hand)
            player_one.add_cards(player_two_hand)
            print(f"Player One wins round {round_num}!")
            at_war = False
        elif player_two_hand[-1] > player_one_hand[-1]:
            player_two.add_cards(player_two_hand)
            player_two.add_cards(player_one_hand)
            print(f"Player Two wins round {round_num}!")
            at_war = False
        else:
            if len(player_one.all_cards) == 0:
                print("Player One is out of cards! Player Two wins!")
                print(f"Rounds played: {round_num}")
                game_on = False
                break

            if len(player_two.all_cards) == 0:
                print("Player Two is out of cards! Player One wins!")
                print(f"Rounds played: {round_num}")
                game_on = False
                break

            print("It's War!!!")
            war_card_count = 5
            if len(player_one.all_cards) < 5:
                war_card_count = len(player_one.all_cards)

            if (len(player_two.all_cards) < 5) and (
                len(player_two.all_cards) < len(player_one.all_cards)
            ):
                war_card_count = len(player_two.all_cards)

            for n in range(war_card_count):
                player_one_hand.append(player_one.remove_card())
                player_two_hand.append(player_two.remove_card())
