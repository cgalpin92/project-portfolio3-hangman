
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_words')

words = SHEET.worksheet('words')



#all_words = words.get_all_values()

#display_rules = rules.get_all_values()

"""
def display_rules():
    rules = SHEET.worksheet('rules')
    list_rules = rules.get_all_values()
    for i in list_rules:
        print(i)
"""  
def display_rules():
    print("The Computer will select a Random Word and display a list of dashes to represent that word\n")
    print("Your aim is to guess what the Random Word is by entering one letter at a time\n")
    print("Enter any letter between 'a' and 'z' where indicated\n")
    print("If the letter is correct it will appear in the correct space within the word\n")
    print("If the letter is incorrect a section of the Hangman's Gallows will be added\n")
    print("You will have 11 attempts to guess the correct word before the Hangman's Gallows are complete and you loose the game\n")


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
print(HANGMAN[11])

display_rules()