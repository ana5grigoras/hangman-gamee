import random

def choose_word():
    cuvinte = ["python", "hangman", "programmer", "calculator", "game", "javascript", "debug", "error", "function", "algorithm", "graphics", "karel", "expressions", "list", "codeinplace"]
    return random.choice(cuvinte)

def my_progress(secret_word, guessed_letters):
    progress = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print(" ".join(progress))

def draw_hangman(tries):
    steps = [
        """
        -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    print(steps[tries-1])

def play_hangman():
    secret_word = choose_word()
    guessed_letters = []
    tries = 7

    print("Welcome to the Hangman game! Have fun!")
    print("Guess the secret word letter by letter.")

    while tries > 0:
        my_progress(secret_word, guessed_letters)
        draw_hangman(tries)
        print(f"You have {tries} tries left")

        letter = input("Your guess is: ").lower()

        if letter in guessed_letters or len(letter) != 1:
            print("You have already entered this letter, or this is not a valid letter. Please try again.")
            continue

        guessed_letters.append(letter)

        if letter not in secret_word:
            tries -= 1
            print("Oops. You guessed it wrong :(")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

    if tries == 0:
        print(f"You lost! The word was: {secret_word}")

if __name__ == "__main__":
    play_hangman()