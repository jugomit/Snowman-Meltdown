import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    print("Welcome to Snowman Meltdown!")

    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0

        while True:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").lower()
            print("You guessed:", guess)
            if len(guess) > 1:
                print("Enter only one letter!")
            elif not guess.isalpha():
                print("You must enter a letter!")
            elif guess in secret_word:
                guessed_letters.append(guess)
            else:
                mistakes += 1

            word_complete = True
            for char in secret_word:
                if char not in guessed_letters:
                    word_complete = False
                    break

            if word_complete:
                print("You guessed the word correctly!")
                break
            elif mistakes == 3:
                print("Snowman melted!")
                break

        while True:
            new_game = input("Do you want to play a new game? (yes or no): ").lower()
            if new_game == "yes":
                break
            if new_game == "no":
                return
            else:
                print("Please enter yes or no: ")
