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

### Future Features

## Data Model

## Testing

### Validator Testing

### Bugs

- __Fixed Bugs__

 - error in terminal when running the random word function. When calling the random_word function had stated print(random.choice(all_words)), when calling this in the terminal received the error "name 'random' is not defined. Did you forget to import 'random'"?
    - imported random at the top of run.py
    - re-ran the function and this time function worked and random word was selected
    - re-ran the function a couple of times and each time a new random word was selected

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
        - Create buildbacks: _needs to be created in this order_
            - Select __Add buildbacks__
            - Select __Python__
            - Save Changes
            - Select __Add buildbacks__
            - Select __NodeJS__
            - Save Changes        
    - Link the Heroku app to the repository
    - Click on __Deploy__

## Credits

### Content
- Words for computer to generate taken from Hangman Words - https://www.hangmanwords.com/words.
- Tutorial on how to create the hangman gallows steps taken from Stack Exchange - https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
- Idea for displaying Rules as print statements taken from existing python hangman game - https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py

### Code
- API settings taken from the Love Sandwiches walkthrough project.