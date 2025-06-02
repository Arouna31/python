from art import logo, vs
from game_data import data
from random import choices


def get_winner_character(character_a, character_b):
    if character_a["follower_count"] > character_b["follower_count"]:
        return {"A": character_a}
    return {"B": character_b}


def logo_printf():
    print("\n" * 100)
    print(logo)


def game():
    is_game_over = False
    current_score = 0
    print(logo)
    while not is_game_over:
        if current_score > 0:
            print(f"You're right Current score: {current_score}")
        choice_characters = choices(data, k=2)
        print(
            f"Compare A: {choice_characters[0]['name']}, a {choice_characters[0]['description']}, from {choice_characters[0]['country']}."
        )
        print(vs)
        print(
            f"Against B: {choice_characters[1]['name']}, a {choice_characters[1]['description']}, from {choice_characters[1]['country']}."
        )
        winner_character = get_winner_character(
            choice_characters[0], choice_characters[1]
        )
        user_choice = input("Who has more followers? Type 'A' or 'B'").upper()

        print(next(iter(winner_character)))
        print(user_choice)
        if next(iter(winner_character)) == user_choice:
            current_score += 1
            logo_printf()

        else:
            logo_printf()
            print(f"Sorry, that's wrong. Final score: {current_score}")
            is_game_over = True


game()
