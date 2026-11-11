import random

# List of words
words = [
    "python",
    "computer",
    "programming",
    "keyboard",
    "internet",
    "developer",
    "software",
    "algorithm"
]

secret_word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

# Hangman drawings
hangman_art = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("\n========== HANGMAN GAME ==========")
print("Guess the hidden word!")
print("You have 6 incorrect attempts.")

while wrong_guesses < max_attempts:

    print(hangman_art[wrong_guesses])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Guessed letters:", sorted(guessed_letters))
    print("Attempts remaining:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The word was:", secret_word.upper())
        break

    guess = input("\nEnter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman_art[wrong_guesses])
    print("\nGame over! You lost.")
    print("The correct word was:", secret_word.upper())

print("\nThank you for playing!")