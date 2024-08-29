# HANGMAN
Hangman is a Python Terminal game which runs in the Code Institute mock terminal Heroku.

Users will play against the computer. The computer will generate a random word and display this as dashes. The user will then try to work out what the word is by guessing individual letters. Each time they guess an incorrect letter a section of the Hangman's gallows is added.

The goal of the game is for the user to guess the word before the Hangman's gallows are complete.

## How to play

The Computer will select a Random Word and display a list of dashes to represent that word
The player's aim is to guess what the Random Word is by entering one letter, between 'a' and 'z', at a time 
If the letter is correct it will appear in the correct space within the word
If the letter is incorrect a section of the Hangman's Gallows will be added
The player will have 11 attempts to guess the correct word before the Hangman's Gallows are complete at which point the player looses the game

## Features

### Existing Features

- __Landing Page__
    - The landing page consists of a Welcome Message and asking the player to either choose to view the rules or play the game.
- __Rules__
    - When selecting Option 1 the Rules for the game are listed
- __Play Game__
    - When selecting Option 2 the Game starts. 
    
        The player will be presented with a message "ready to play". 

        A list of dashes will represent the word that the computer has randomly selected.

        An input will appear asking the player to enter a letter

        If a number or special character is entered instead of a letter then a message will appear stating the player must enter a letter.

        If a letter is entered and matches a letter within the hidden word then that letter will appear within the hidden word section

        If a letter is entered that does not match a letter within the hidden word then a section of the hangman's gallows appears. This will continue until a correct letter is entered.

### Future Features

## Data Model

## Testing

### Validator Testing

### Bugs

- __Fixed Bugs__

    - Error in terminal when running the random word function. When calling the random_word function had stated print(random.choice(all_words)), when calling this in the terminal received the error "name 'random' is not defined. Did you forget to import 'random'"?
        - imported random at the top of run.py
        - re-ran the function and this time function worked and random word was selected
        - re-ran the function a couple of times and each time a new random word was selected
    
    - Error replacing the random selected word with dashes to keep the word hidden.
        - First issue was that nothing appeared when function was called. No random word selected. I realised I had missed the print method at the end of the function. Added this in.
        - Now when the function was called a single dash appeared. Had intended this to be a dash for each character of the chosen word. Current variable written as hidden_word = "_" * len(all_words). Researched online and surmised issue may be to do with the previous variable all_words = words.get_all_values(). This returns a list data type e.g. ['zigzag']. I believe the length of this was being perceived as a value of 1. Changed the value to all_words = words.col_values(1). This returns a string data type, e.g. zigzag. This hidden_word variable now returns dashes for each individual letter of the selected word e.g. _ _ _ _ _ _
    
    - Error line too long in pep8 Python validator.
        - When running an initial test within pep8 python validation, error resulted for line to long for valid_input variable. The data within this variable was a list of the letters of the alphabet to check which I was using to check against the player's guess to ensure it was a valid letter and not a number. However due to this exceeding the 79 character limit I searched online for another solution to validify a letter input. Found a suggestion to use isalpha().
        - Initially tried changing just the value of the variable from a list of letters to isalpha(). However when running this in the terminal received the error that isalpha() is not defined.
        - Checked online suggestion further and decided to change the if statement to a for statement and to include the isalpha() argument within this statement. Statement now states:
            - for i in guess:
                if i.isalpha():
                    print(f"you entered {guess}")
                else:
                    print(You must enter a letter)
        - When running this within the terminal the validation test was successfull, when entering a number the else statement runs, when entering a letter the if statment runs.
    
- __Unfixed Bugs__

## Deployment

This project was deployed using the Code Institute's mock terminal for Heroku.

- __Steps for deployment:__
    - Fork or clone this repository
    - Create a new Heroku app
        - Login to Heroku and select __Create New App__
        - Create app name
        - Select your __region__
        - Select __Create App__
    - Change Heroku Settings
        - Select __Settings__
        - Scroll down to __Config Var__ section and select __reveal config var__
        - Enter the following information into the __Key__ and __value__ inputs:
            - __Key:__ CREDS
            - __Value:__ Copy all content from the creds.json file and paste into the values box.
        - Select __Add__
        - Add another config var with the following information:
            - __Key:__ PORT
            - __Value:__ 8000
        - Create buildpacks: _needs to be created in this order_
            - Select __Add buildpacks__
            - Select __Python__
            - Select __Add Buildpack__
            - Select __Add buildpacks__
            - Select __NodeJS__
            - Select __Add Buildpack__     
    - Link the Heroku app to the repository:
        - Select __Deploy__ from the top of the page.
        - Scroll down to __Deployment method__
        - Select __GitHub. Connect to GitHub__
        - Enter you repository name and click search
        - Select connect next to your repository name
    - Click on __Deploy__

## Credits

### Content
- Words for computer to generate taken from Hangman Words - https://www.hangmanwords.com/words.
- Tutorial on how to create the hangman gallows steps taken from Stack Exchange - https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
- Idea for displaying Rules as print statements taken from existing python hangman game - https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py

### Code
- API settings taken from the Love Sandwiches walkthrough project.
- Code for displaying the randomly selected word from the google worksheet as a series of dashes for the length of the word taken from existing pythong hangman game - https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py 
- Code to check validation of player's guess taken from Stack Overflow - https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python#:~:text=By%20using%20str.,if%20it%20is%20a%20letter. 