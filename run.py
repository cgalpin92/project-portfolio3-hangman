
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
    """
    Displays the rules when called
    """
    print("The Computer will select a Random Word and display a list of dashes to represent that word\n")
    print("Your aim is to guess what the Random Word is by entering one letter at a time\n")
    print("Enter any letter between 'a' and 'z' where indicated\n")
    print("If the letter is correct it will appear in the correct space within the word\n")
    print("If the letter is incorrect a section of the Hangman's Gallows will be added\n")
    print("You will have 11 attempts to guess the correct word before the Hangman's Gallows are complete and you loose the game\n")



def play():
    words = SHEET.worksheet('words')
    all_words = words.col_values(1)
    random_word = random.choice(all_words)
    print(random_word)
    print(random_word[0])
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
            x = ''.join(guess if random_word[i] == guess else hidden_word[i] for i in range(len(random_word)))
            print(x)
        else:
            print(hidden_word)
                        
    check_answer()

def run_game():
    home()

run_game()
