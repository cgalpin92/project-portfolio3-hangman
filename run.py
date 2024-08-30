
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

attempts_taken = 0
attempts_left = 11
build_pictures = 0
used_letters = []
random_word = None
hidden_word = None
game_play = True

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
    print("and you will loose\n")
    print("\nstarting game...\n")



def start_game():
    global hangman_picures
    hangman_picures = 0
    global attempts_taken
    attempts_taken = 0
    print('START GAME attempts_taken: ', attempts_taken)
    print(f"Hi {username}\n")
    display_rules()


def select_random_word():
    """
    selects random word from googlesheets
    """
    words = SHEET.worksheet('words')
    all_words = words.col_values(1)
    global random_word
    random_word = random.choice(all_words)
    # print(random_word)  # will remove once code complete


def hide_random_word():
    """
    changes the letters within the random word to -
    """
    global hidden_word
    hidden_word = "-" * len(random_word) + "\n"
    print(hidden_word)


def guess_input():
    """
    creates the input for player to enter their guess
    """
    global guess
    global end_game
    global game_play
    global attempts_taken
    if attempts_taken == 20:
        game_play = False
        print("You have run out of attempts\n")
        print(f"The word was {random_word}\n")
        print("Game Over!!\n")
    elif attempts_left == 0:
        game_play = False
        print("You have run out of attempts\n")
        print(f"the word was {random_word}\n")
        print("Game Over!!\n")
    elif "-" not in hidden_word:
        game_play = False
        print("Contratulations!!\n")
        print(f"You correctly guessed {random_word}\n")
        print("Game Over!!\n")
    while game_play is True:   
        print('GUESS INPUT attempts_taken: ', attempts_taken)
        guess = input("Enter Letter Below: \n")
        check_guess_input()




def check_guess_input():
    """
    validates that the guess is a letter
    if the guess is a letter attempts will increase by one
    the letter will be added to the used letters list
    and the hidden word will be updated with the letter
    if the guess is not a letter the user will be notified
    and they will be asked to enter a guess again
    attempts will not increase
    """
    global attempts_taken
    global used_letters
    global game_play
    print('CHECK GUESS INPUT attempts_taken: ', attempts_taken)
    for i in guess:
        if i.isalpha():
            print('IF BLOCK attempts_taken: ', attempts_taken)
            print(f"You entered {guess} \n")
            attempts_taken += 1
            print('INCREMENT attempts_taken: ', attempts_taken)
            used_letters += guess
            print(used_letters)
            update_hidden_word()
        else:
            print("You must enter a letter\n")
            guess_input()


def update_hidden_word():
    global hidden_word
    global build_pictures
    if guess in random_word:
        positions = [i for i, a in enumerate(random_word) if a == guess]
        hidden_word_list = list(hidden_word)
        for num in positions:
            hidden_word_list[num] = guess
        hidden_word = "".join(hidden_word_list)
        print(hidden_word)
    else:
        build_pictures += 1
        print('build_pictures stage', build_pictures)
        update_hangman()
    guess_input()
        

def update_hangman(): 
    global attempts_left
    if guess != random_word:
        attempts_left -= 1
        print(f"you have {attempts_left} attempts left")
        print(HANGMAN[build_pictures])
        print(hidden_word)
    else:
        print("resetting picture")
            


def main():
    start()
    start_game()
    select_random_word()
    hide_random_word()
    guess_input()


main()
