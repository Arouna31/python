# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

has_player = True
players_bids = {}
winner_name = ""
higher_score = 0

print(logo)


def is_game_continue(answer):
    if answer != "no":
        return True
    return False


while has_player:
    player_name = input("What is your name ? ")
    player_bid = int(input("What is your bid ? : $"))
    players_bids[player_name] = player_bid
    has_new_player = input("Are there any other bidders ? Type 'yes or no' .\n   ")
    has_player = is_game_continue(has_new_player)

for player in players_bids:
    if players_bids[player] > higher_score:
        higher_score = players_bids[player]
        winner_name = player

print(f"The winner is {winner_name} with a bid of ${higher_score}")
