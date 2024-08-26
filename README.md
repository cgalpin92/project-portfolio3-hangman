# HANGMAN
Hangman is a Python Terminal game which runs in the Code Institute mock terminal Heroku.

Users will play against the computer. The computer will generate a random word and display this as dashes. The user will then try to work out what the word is by guessing individual letters. Each time they guess an incorrect letter a section of the Hangman's gallows is added.

The goal of the game is for the user to guess the word before the Hangman's gallows are complete.

## How to play

## Features

### Existing Features

### Future Features

## Data Model

## Testing

### Validator Testing

### Bugs

- __Fixed Bugs__

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

### Code
- API settings taken from the Love Sandwiches walkthrough project.