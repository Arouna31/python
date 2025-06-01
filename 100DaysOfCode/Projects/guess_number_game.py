from art import logo
from random import randint


def get_attempts_number(difficulty):
    if difficulty == "hard":
        return 5
    return 10


def guessing(user_guessed_number, computer_guessed_number, attempts):
    # print(f"{user_guessed_number} {computer_guessed_number}")
    if attempts > 0:
        if user_guessed_number > computer_guessed_number:
            print("Too high.")
        if user_guessed_number < computer_guessed_number:
            print("Too low.")
        if user_guessed_number != computer_guessed_number:
            print("Guess again")


def main():
    gold_number = randint(1, 100)

    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard':")
    attempts_number = get_attempts_number(difficulty_choice)
    is_game_over = False
    while attempts_number > 0 and not is_game_over:
        print(f"You have {attempts_number} attempts remaining to guess the number.")
        result_user_guess_number = int(input("Make a guess : "))
        if result_user_guess_number == gold_number:
            print(f"You got it! The answer was {gold_number}.")
            is_game_over = True

        attempts_number -= 1
        guessing(result_user_guess_number, gold_number, attempts_number)

        if attempts_number == 0:
            print("You've run out of guesses. Refresh the page to run again.")


main()
