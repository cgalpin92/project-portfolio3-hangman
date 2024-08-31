
import gspread
from google.oauth2.service_account import Credentials
import random

"""
Guidance on following Constants taken from Love Sandwiches Project
SCOPE
CREDS
SCOPED_CREDS
GSPREAD_CLIENT
SHEET
"""
# constant variables
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

TOTAL_ATTEMPTS_ALLOWED = 20

# global variables
attempts_taken = 0
attempts_left = 11
build_pictures = 0
used_letters = []
random_word = None
hidden_word = None
game_play = True

def start():

    """
    Function to start the game.
    Runs when terminal is launched.
    Explains what Hangman is.
    Asks the user to enter a username to proceed.
    Username can be any number of letters or digits but cannot be blank.
    If no username is entered will re-ask until username entered.
    Will then proceed to start the game.
    """
    print("Welcome to Hangman\n")
    print(HANGMAN[11])
    print("Hangman is a guessing game for 2 or more players\n")
    print("In this game you will be playing against the computer\n")
    print("One player thinks of a word\n")
    print("And the other player tries to guess the word within a certain")
    print("number of guesses or before the Hangman image above is complete\n")
    print("To play this Hangman game please enter a username to proceed\n")
    while True:
        global username
        username = input("Enter username here:  \n")
        if username.isalpha():
            break
        elif username.isdigit():
            break
        else:
            print("You have not entered a username\n")
            print("You must enter a username to proceed\n")
    print("\nRules Loading...\n")
    display_rules()
    


def display_rules():
    """
    Function to display the rules when player enters a valid username.
    Player is then asked if they would like to proceed and play
    the game. If they enter y the game starts, if they enter
    n the screen will return to home screen
    """
    print(f"Hi {username}\n")
    print("The Computer will select a word at random\n")
    print("A list of dashes will appear to represent that word\n")
    print("Your aim is to guess the word either by entering a letter,")
    print("or by entering an entire word (if you think you know it)\n")
    print("Enter any letter between 'a' and 'z' in the space provided\n")
    print("If you guess a correct letter or word, the computer will")
    print("replace a dash within it's correct position within the word\n")
    print("If you are wrong the Hangman picture will start to build\n")
    print("After 11 incorrect guesses the Hangman picture will be complete\n")
    print("To win the game you have to guess the correct word either within")
    print("20 attempts or before the Hangman picture is complete\n")
    play = input("Ready to Play? Enter y or n: \n")
    if play.lower() == "y":
        print("\nstarting game...\n")
        start_game()
    elif play.lower() == "n":
        print("Returning to home screen...")
        start_game()    
    else:
        print("You did not enter a valid answer. Please enter Y or N:")



def start_game():
    """
    Function to start the game once the player has entered y.
    HANGMAN Pictures and attempts taken are set to zero.
    Number of attempts taken is printed to terminal.
    display_rules function is called.
    """
    global hangman_picures
    hangman_picures = 0
    global attempts_taken
    attempts_taken = 0


def select_random_word():
    """
    Function for the computer to select a random word from googlesheets.
    """
    words = SHEET.worksheet('words')
    all_words = words.col_values(1)
    global random_word
    random_word = random.choice(all_words)
    print(random_word)  # will remove once code complete


def hide_random_word():
    """
    Function to change the letters within the random word to '-'.
    """
    global hidden_word
    hidden_word = "-" * len(random_word) + "\n"
    print(f"Your word is {hidden_word}")


def guess_input():
    """
    Function to check if the game play is true or false
    If true will create the input for player to enter their guess
    If false game will end and the appropriate print statements 
    will print for the player
    """
    global guess
    global end_game
    global game_play
    global attempts_taken
    if attempts_taken == TOTAL_ATTEMPTS_ALLOWED:
        game_play = False
        print("You have run out of attempts\n")
        print(f"The word was {random_word}\n")
        print("Game Over!!!\n")
        play_again()
    elif attempts_left == 0:
        game_play = False
        print("The Hangman picture is complete\n")
        print(f"the word was {random_word}\n")
        print("Game Over!!!\n")
        play_again()
    elif "-" not in hidden_word:
        game_play = False
        print("Contratulations!!!\n")
        print(f"You correctly guessed {random_word}\n")
        print("Game Over!!!\n")
        play_again()
    while game_play is True:   
        print(f'Attempts: {attempts_taken} out of {TOTAL_ATTEMPTS_ALLOWED}\n')
        guess = input("Enter Letter Below: \n")
        guess = guess.lower()
        check_guess_input()




def check_guess_input():
    """
    Function to validates that the guess is a letter.
    If the guess is a letter attempts will increase by one.
    The letter will be added to the used letters list
    and the hidden word will be updated with the letter.
    The used letter list is printed to the terminal.
    If the guess is not a letter the user will be notified
    and they will be asked to enter a guess again.
    Attempts will not increase
    """
    global attempts_taken
    global used_letters
    global game_play
    for i in guess:
        if i.isalpha():
            print(f"\nYou entered {guess} \n")
            attempts_taken += 1
            used_letters += guess
            update_hidden_word()

            
        else:
            print("You must enter a letter\n")
            guess_input()



def update_hidden_word():
    """
    Function to update the hidden word if the player guesses the correct letter.
    If the player guesses an incorrect letter the hangman pictures will start to build.
    Section within if statement taken from existing hangman game and Stack Overflow sites:
    https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py#L510
    https://stackoverflow.com/questions/44307988/find-all-occurrences-of-a-character-in-a-string
    """
    global hidden_word
    global build_pictures
    global attempts_left
    global attempts_taken
    global used_letters
    if guess == random_word:
        hidden_word = random_word
    elif guess in random_word:
        """
        taken from existing hangman game and stack overflow sites listed above
        """
        
        # positions = [i for i, a in enumerate(random_word) if a == guess]
        hidden_word_list = list(hidden_word)
        # for num in positions:
        for index, letter in enumerate(random_word):
            if letter == guess:
                hidden_word_list[index] = letter
            
            # hidden_word_list[num] = guess
        hidden_word = "".join(hidden_word_list)
        print(f"WELL DONE!! {guess} was correct\n")
        print(hidden_word)
        print(f"letters guessed so far: {used_letters}\n")
    else:
        """
        Guidance for building below code taken from above hangman game site
        """
        print(f"Sorry, {guess} was incorrect")
        build_pictures += 1
        print(f'Hangman Picture: {build_pictures} out of 11')
        if guess != random_word:
            attempts_left -= 1
            print(HANGMAN[build_pictures])
            print(f"letters guessed so far: {used_letters}\n")
            print(hidden_word)
    guess_input()    
    
            
def play_again():
    """
    Function to ask the player if they would like to play again after the game
    has ended.
    If they select Y the game restarts and the restart function is called.
    If they select N the game ends.
    If they do not answer Y, y, N or n they will be asked to enter a valid
    answer.
    """
    print("Would you like to play again?\n")
    print("Enter Y for Yes or N for No\n")

    answer_input = input("Y or N \n")
    if answer_input.upper() == "Y":
        print("restarting...")
        restart()
    elif answer_input.upper() == "N":
        print(f"Thank you {username} for playing\n")
        print("Ending Game...\n")
    else:
        print("You did not enter a valid answer, Please answer Y or N\n")


def restart():
    """
    Function to restart game
    Global variables are reset.
    random_word(), hide_random_word() and guess_input() functions are recalled.
    """
    global attempts_taken
    global attempts_left
    global build_pictures
    global used_letters
    global random_word
    global hidden_word
    global game_play
    attempts_taken = 0
    attempts_left = 11
    build_pictures = 0
    used_letters = []
    random_word = None
    hidden_word = None
    game_play = True
    select_random_word()
    hide_random_word()
    guess_input()  

def main():
    """
    main function which runs the terminal game
    """
    start()
    select_random_word()
    hide_random_word()
    guess_input()
    
if __name__ == "__main__":
    main()
