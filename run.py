
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

"""
def home():
    print("Welcome to Hangman\n")
    print("Please choose an option below to proceed\n")
    print("Option 1: Rules\n")
    print("Option 2: Play Game\n")

    option = input("Enter option here:  \n")

    option_data = int(option)

    if option_data == 1:
        display_rules()
    elif option_data == 2:
        print("\nready to play\n")
        play()
    else:
        print("Please enter a valid option\n")
        home()


def display_rules():
    
    #Displays the rules when called
    
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


def play():
    words = SHEET.worksheet('words')
    all_words = words.col_values(1)
    random_word = random.choice(all_words)
    print(random_word)  # Will remove once code complete
    hidden_word = "_" * len(random_word) + "\n"
    print(hidden_word)
    
    guess = input("Enter Letter Below: \n")
    for i in guess:
        if i.isalpha():
            print(f"you entered {guess}\n")
        else:
            print("You must enter a letter\n")
    
    def check_answer():
        if guess in random_word:
            x = ''.join(guess if random_word[i] == guess
                        else hidden_word[i] for i in range(len(random_word)))
            new_hidden_word = x
            print(new_hidden_word)
        else:
            print(HANGMAN[1])
                        
    check_answer()


def run_game():
    home()


run_game()
"""

def start():

    """
    Runs when terminal is launched
    Explains what Hangman is
    Asks the user to enter a username to proceed
    If no username is entered will re-ask until username entered
    Will then proceed to start the game
    """
    print("Welcome to Hangman\n")
    print("Welcome to Hangman\n")
    print(HANGMAN[11])
    print("what hangman game is")
    print("Please enter a username below to proceed\n")
	
    while True:
        username = input("Enter username here:  \n")
        if username.isalpha():
            break
        elif username.isdigit():
            break
        else:
            print("You have not entered a username, please enter a username to proceed")
    print("game loading...")


def main():
    start()


main()