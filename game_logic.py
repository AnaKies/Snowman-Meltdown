import random
import ascii_art


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Selects a random word from the list.
    :return: a random word from the list.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the snowman stage for the current number of mistakes.
    Registers a mistake, evaluates and displays a game over.
    :param mistakes: number of mistakes that the user did by guessing the word
    :param secret_word: string that should be guessed
    :param guessed_letters: list with letters that the user has already guessed
    :return: True if a letter is not in the word, False otherwise.
    None if the game is over.
    """
    print(ascii_art.STAGES[mistakes])

    if mistakes >= len(ascii_art.STAGES) - 1:
        print(f"Game Over! The secret word was: {secret_word}")
        return None

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            is_wrong = True
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")
    return is_wrong

def check_wrong_input(user_letter):
    """
    Checks if user enters a single letter, and it is not a digit.
    :param user_letter: guessed letter from user input
    """
    if len(user_letter) != 1:
        raise Exception(f"Only single characters are allowed! You entered {user_letter}.")
        return

    if user_letter.isdigit():
        raise Exception(f"Digits are not allowed! You entered {user_letter}.")


def play_game():
    """
    Runs the game logic and displays the game state.
    :return: None
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    while True:
        is_wrong = display_game_state(mistakes, secret_word, guessed_letters)

        if is_wrong is True:
            mistakes += 1
        elif is_wrong is None:
            break

        user_letter = input("Guess a letter: ").lower()
        guessed_letters.append(user_letter)
        print("You guessed:", user_letter)
        check_wrong_input(user_letter)
