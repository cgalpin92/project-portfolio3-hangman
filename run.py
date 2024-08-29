
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')


HANGMAN = [
    """
    """,
    """
    |
    |
    |
    |
    |
    |
    |
    |
    """,
    """
    |
    |
    |
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |
    |
    |
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |
    |
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |         O
    |
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |         O
    |         +
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |         O
    |      +--+
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |         O
    |      +--+--+
    |
    |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |         O
    |      +--+--+
    |         |
    |         |
    |
    |
    |
    ---------------
    """,
    """
    -----------
    |         |
    |         O
    |      +--+--+
    |         |
    |         |
    |        |
    |        |
    |
    ---------------

    """,
    """
    -----------
    |         |
    |         O
    |      +--+--+
    |         |
    |         |
    |        | |
    |        | |
    |
    ---------------
    """
]


def start():

    """
    Runs when terminal is launched
    Explains what Hangman is
    Asks the user to enter a username to proceed
    If no username is entered will re-ask until username entered
    Will then proceed to start the game
    """
    print("Welcome to Hangman\n")
    print(HANGMAN[11])
    print("what hangman game is")
    print("Please enter a username below to proceed\n")
    while True:
        global username
        username = input("Enter username here:  \n")
        if username.isalpha():
            break
        elif username.isdigit():
            break
        else:
            print("You have not entered a username\n")
            print("please enter a username to proceed\n")
    print("game loading...\n")


def display_rules():
    """
    Displays the rules when called
    """
    print("The Computer will select a word at random\n")
    print("A list of dashes will appear to represent the word\n")
    print("Your aim is to guess the word one letter at a time\n")
    print("Enter any letter between 'a' and 'z'\n")
    print("If you are right the letter will replace a dash\n")
    print("If you are wrong a section of the Hangman's Gallows is added\n")
    print("You will have 11 attempts to guess the correct word\n")
    print("Guess before those 11 attepts are up and you win\n")
    print("If you don't guess before the Hangman's Gallows are complete...\n")
    print("you loose\n")
    print("\nstarting game...\n")


def start_game():
    global hangman_picures
    hangman_picures = 0
    global attempts
    attempts = 0
    print(f"Hi {username}\n")
    display_rules()


def select_random_word():
    words = SHEET.worksheet('words')
    all_words = words.col_values(1)
    global random_word
    random_word = random.choice(all_words)
    print(random_word)  # will remove once code complete


def hide_random_word():
    global hidden_word
    hidden_word = "_" * len(random_word) + "\n"
    print(hidden_word)


def guess_input():
    global guess
    guess = input("Enter Letter Below: \n")
    check_guess_input()


def check_guess_input():
    global attempts_taken
    for i in guess:
        if i.isalpha():
            print(f"You entered {guess} \n")
            attempts_taken = attempts + 1
            update_hidden_word()
        else:
            print("You must enter a letter\n")
            guess_input()


def update_hidden_word():
    global new_hidden_word
    global build_pictures
    if guess in random_word:
        x = "".join(guess if random_word[i] == guess
                    else hidden_word[i]for i in range(len(random_word)))
        new_hidden_word = x
        print(new_hidden_word)
        guess_input()
    else:
        build_pictures = hangman_picures + 1
        update_hangman()
        guess_input()


def update_hangman():
    if guess != random_word:
        print(HANGMAN[build_pictures])
    else:
        print("resetting picture")


def game_play():
    global game_play
    if attempts_taken <= 6:
        game_play = True
        print("True")
    else:
        game_play = False
        print("False")


def main():
    start()
    start_game()
    select_random_word()
    hide_random_word()
    guess_input()
    game_play()


main()
