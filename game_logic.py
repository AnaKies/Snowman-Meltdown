import random
import ascii_art
from colorama import init, Fore


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
SEPARATORS_NUMBER = 40

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
    :return: True if the game is won, False if game is over, None otherwise
    """
    print(Fore.LIGHTBLUE_EX + "*" * SEPARATORS_NUMBER)
    print(Fore.BLUE + ascii_art.STAGES[mistakes])
    print(Fore.LIGHTBLUE_EX +  "." * SEPARATORS_NUMBER)

    # last stage of a snowman (hat) means game over
    if mistakes >= len(ascii_art.STAGES) - 1:
        print(Fore.RED + f"💀Game Over! The secret word was: {secret_word}")
        return False # game over

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(Fore.GREEN +  "Word: ", display_word)
    print(Fore.LIGHTBLUE_EX +  "." * SEPARATORS_NUMBER)

    if not "_" in display_word:
        print("🎉Congratulations, you saved the snowman!")
        return True # game is won
    return None # game go further


def check_wrong_input(user_letter):
    """
    Checks if user enters a single letter, and it is not a digit.
    :param user_letter: guessed letter from user input
    :return: True if the user did a wrong input, False otherwise.
    """
    if len(user_letter) != 1:
        print(Fore.RED +  f"Only single characters are allowed! You entered {user_letter}.")
        wrong_input = True
        return wrong_input

    if user_letter.isdigit():
        print(Fore.RED +  f"Digits are not allowed! You entered {user_letter}.")
        wrong_input = True
        return wrong_input

    wrong_input = False
    return wrong_input


def init_new_game():
    """
    Initializes a new game of snowman.
    :return: secret word as string, guessed letters as list, mistakes as integer
    """
    secret_word = get_random_word()
    print(Fore.MAGENTA + "❄️Welcome to Snowman Meltdown!")
    print(Fore.LIGHTYELLOW_EX + "Secret word selected: " + secret_word)  # for testing, later remove this line
    guessed_letters = []
    mistakes = 0

    return mistakes, secret_word, guessed_letters



def play_game():
    """
    Runs the game logic and displays the game state.
    :return: None
    """
    init(autoreset = True) # initialise colorama module with reset of current color
    mistakes, secret_word, guessed_letters = init_new_game()
    while True:
        try:
            game_is_won = display_game_state(mistakes, secret_word, guessed_letters)

            # stop the game if it was won or lost
            if game_is_won is not None:
                restart_game = input("Restart game? Y/N? ")
                if restart_game.lower() == "n":
                    break
                elif restart_game.lower() == "y":
                    mistakes, secret_word, guessed_letters = init_new_game()
                    continue
                else:
                    print("Print Y or N")
                    continue

            user_letter = input("Guess a letter: ").lower()
            wrong_user_input = check_wrong_input(user_letter)

            if wrong_user_input is False:
                guessed_letters.append(user_letter)

            letter_is_in_secret_word = user_letter in secret_word

            if not letter_is_in_secret_word is True:
                mistakes += 1
        except Exception as error:
            print(Fore.RED +  f"Error in program: {error}")
