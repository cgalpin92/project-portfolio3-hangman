
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

rules = SHEET.worksheet('rules')

#all_words = words.get_all_values()

display_rules = rules.get_all_values()



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

print(display_rules)