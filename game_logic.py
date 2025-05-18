import random

from colorama import init, Fore

# Module with graphic for different stages of snowman melting.
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
SEPARATORS_NUMBER = 40


def get_random_word():
    """
    Selects a random word from the list.
    :return: A random word from the list.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the snowman stage for the current number of mistakes.
    Registers a mistake, evaluates and displays a game over.
    :param mistakes: Number of mistakes that the user did by guessing the word
    :param secret_word: string that should be guessed
    :param guessed_letters: list with letters that the user has already guessed
    :return: True if the game is won, False if the game is over, None otherwise
    """
    print(Fore.LIGHTBLUE_EX + "*" * SEPARATORS_NUMBER)
    print(Fore.BLUE + ascii_art.STAGES[mistakes])
    print(Fore.LIGHTBLUE_EX + "." * SEPARATORS_NUMBER)

    # the last stage of a snowman (hat) means game over
    if mistakes >= len(ascii_art.STAGES) - 1:
        print(Fore.RED + f"💀Game Over! The secret word was: {secret_word}")
        return False  # game over

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(Fore.GREEN + "Word: ", display_word)
    print(Fore.LIGHTBLUE_EX + "." * SEPARATORS_NUMBER)

    if "_" not in display_word:
        print("🎉Congratulations, you saved the snowman!")
        return True  # the game is won
    return None  # game go further


def user_input_is_wrong(user_letter, guessed_letters):
    """
    Checks if a user enters a single letter, and it is not a digit.
    :param guessed_letters: letters that the user has already guessed.
    :param user_letter: guessed a letter from user input
    :return: True if the user did a wrong input, False otherwise.
    """
    if user_letter in guessed_letters:
        print(Fore.RED + f"You have already guessed the letter {user_letter}.")
        return None

    if len(user_letter) != 1:
        print(Fore.RED +
              f"Only single characters are allowed! "
              f"You entered {user_letter}.")
        return True

    if user_letter.isdigit():
        print(Fore.RED + f"Digits are not allowed! You entered {user_letter}.")
        return True
    return False


def init_new_game():
    """
    Initializes a new game of snowman.
    :return: Secret word as string,
    guessed letters as a list,
    mistakes as integer
    """
    secret_word = get_random_word()
    print(Fore.MAGENTA + "❄️Welcome to Snowman Meltdown!")
    guessed_letters = []
    mistakes = 0

    return mistakes, secret_word, guessed_letters


def play_game():
    """
    Runs the game logic and displays the game state.
    If the user inputs the wrong letter, the snowman melts.
    If the user inputs a number or a string or the same letter,
    a message is displayed. It does not count as a mistake.
    The game is won when the user guesses all the letters
    while the snowman still has an eye.
    The game is over when the snowman reaches the last stage with an eye.
    :return: None
    """
    # initialise colorama module with reset of current color
    init(autoreset=True)
    mistakes, secret_word, guessed_letters = init_new_game()
    while True:
        try:
            game_is_won = display_game_state(mistakes,
                                             secret_word,
                                             guessed_letters)
            # stop the game if it was won or lost
            if game_is_won is not None:
                restart_game = input("Restart game? Y/N? ")
                if restart_game.lower() == "n":
                    break
                if restart_game.lower() == "y":
                    print()
                    mistakes, secret_word, guessed_letters = init_new_game()
                    continue
                print("Print Y or N")
                continue

            user_letter = input("Guess a letter: ").lower()
            wrong_user_input = user_input_is_wrong(user_letter,
                                                   guessed_letters)

            if wrong_user_input is False:
                guessed_letters.append(user_letter)
                letter_is_in_secret_word = user_letter in secret_word

                if letter_is_in_secret_word is not True:
                    mistakes += 1

        except Exception as error:
            print(Fore.RED + f"Error in program: {error}")
