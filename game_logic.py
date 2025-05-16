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
    :return: True if the game is over, None otherwise
    """
    print(ascii_art.STAGES[mistakes])

    # last stage of a snowman (hat) means game over
    if mistakes >= len(ascii_art.STAGES) - 1:
        print(f"Game Over! The secret word was: {secret_word}")
        game_is_over = True
        return game_is_over

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def check_wrong_input(user_letter):
    """
    Checks if user enters a single letter, and it is not a digit.
    :param user_letter: guessed letter from user input
    :return: True if the user did a wrong input, False otherwise.
    """
    if len(user_letter) != 1:
        print(f"Only single characters are allowed! You entered {user_letter}.")
        wrong_input = True
        return wrong_input

    if user_letter.isdigit():
        print(f"Digits are not allowed! You entered {user_letter}.")
        wrong_input = True
        return wrong_input

    wrong_input = False
    return wrong_input

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
        try:
            game_is_over = display_game_state(mistakes, secret_word, guessed_letters)
            if game_is_over:
                break

            user_letter = input("Guess a letter: ").lower()
            wrong_user_input = check_wrong_input(user_letter)

            if wrong_user_input is False:
                guessed_letters.append(user_letter)

            letter_is_in_secret_word = user_letter in secret_word

            if not letter_is_in_secret_word is True:
                mistakes += 1
        except Exception as error:
            print(f"Error in program: {error}")
