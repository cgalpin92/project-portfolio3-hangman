# HANGMAN
Hangman is a Python Terminal game which runs in the Code Institute mock terminal Heroku.

Hangman is a word guessing game. You can read more about it on Wikipedia - https://en.wikipedia.org/wiki/Hangman_(game)

Players will play against the computer which will generate a random word and display this as dashes to hide it from the player. 
The player will then try to work out what the word is by guessing individual letters or by guessing a whole word. 
The goal of the game is for the player to guess the word.

Here is a live version of my project:

## User Experience

- As a user I want to understand the rules of the game.
- As a user I want beat the computer and guess the word before my guesses run out.

## How to play

1. The Computer will select a word at random.

2. A list of dashes will appear to represent that word.

3. The player's aim is to guess the correct word either by entering a letter or by entering an entire word, if they think they know it.

4. They can enter any letter between 'a' and 'z' in the space provided to them.

5. If the player guesses a correct letter or word, the computer will replace a dash within the correct position within the hidden word.

6. If the player guesses incorrectly, the Hangman picture will start to build. After 11 incorrect guesses the Hangman picture will be complete.

7. To win the game, the player must correctly guess the word either within 20 attempts or before the Hangman picture is complete.

## Features

### Existing Features

- __Landing Page__
    - The landing page consists of a Welcome Message.
    - A full image of the Hangman picture is displayed.
    - There is brief description about what Hangman is.
    - The player is asked to enter a username.
- __Rules__
    - Statement prints to tell the player that the Rules are loading.
    - The rules are displayed.
    - The player is then asked if they are ready to play the game.
- __Play Game__
    - Statement prints to tell the player that the game is starting.
    - A list of dashes is presented to the player with a statement telling them that this is their hidden word.
    - If this is the first time the game is played, a statement is printed to say they have taken 0 attempts.
    - An input is presented for the player to enter a letter or word.
    - A statement is printed to confirm the player’s input.
        - If input is word and its correct the full word shows, the player is congratulated and asked if they would like to play again.
        - If correct:
            - The correct letter will appear within the hidden word.
            - The letter will appear within the used letters field.
            - The player is asked to enter another letter.
        - If incorrect:
            - The Hangman picture starts to build.
            - The letter will appear within the used letters field.
            - The player is asked to enter another letter.
    - Game play continues until either the correct word is guessed, or the Hangman image is complete.
    - At which point player is asked if they want to play again. 
        - If they do game will reload.
        - If they choose to end the game statement will print to show game ending.

### Future Features
- I would like to add a scoreboard to record who wins each game - player or computer
- I would like to add levels to the game so that the user can increase difficulty - longer letters to guess.
- I would like to add categories for the different types of words.

## Data Model
 - I decided to use a hierarchy of functions as the main data model for running this game. 
    - The main function is the parent function for this game.
    - Each subsequent function is either a child of the main function, or a further child node of these subsequent functions which will run only once the conditions of its parent function have been met.
 - There are Constant variables listed at the start of the code to hold the unmodified data such as the APIs that the program should access and the Hangman pictures.
 - I have used some global variables which will be modified as the game is played and that can be accessed by multiple functions.
 - Within the functions I have used while loops to run the continuation of the game and if statements to validate user inputs.
 - Below is the flowchart I created using Lucid to help organise the flow of the game and the creation of the parent and child functions.

## Testing

### Validator Testing

-__PEP8 Testing__

    - After passing the final code through the PEP8 linter I can confirm there are no errors.

-__Manual Testing__

    - When running the game, I ran the following tests to see if they would cause any errors within the game.
        - I entered an extremely long username - this did not break the game, each time the username field was printed, the username I had entered printed. Whilst not ideal to have such a long username, this does not affect the running of the code.
        - I have entered a capital letter within the inputs that request either a Y or N or a letter (guess input). Each time the code will convert these inputs to a lower case so that the code does not break.
        - I have entered numbers where a letter or word is specified, this does not break the game, the player is asked to re-enter a valid letter as the code specifies.
    
    - I have successfully tested the game in both my local terminal within GitHub and the Code Institute Heroku terminal.

### Bugs

- __Fixed Bugs__

    - Error in terminal when running the random word function. 
        - When calling the random_word function I had previously written print(random.choice(all_words)). When calling this in the terminal received the error "name 'random' is not defined. Did you forget to import 'random'"?
        - Imported random at the top of run.py we suggested by the python terminal.
        - This fixed the error as when each time re-running the function a random word was selected.
    
    - Error replacing the random selected word with dashes to keep the word hidden.
        - First issue was that nothing appeared when function was called. No random word selected. I realised I had missed the print method at the end of the function. Added this in.
        - Now when the function was called a single dash appeared. Had intended this to be a dash for each character of the chosen word. Current variable written as hidden_word = "_" * len(all_words). Researched online and surmised issue may be to do with the previous variable all_words = words.get_all_values(). This returns a list data type e.g. ['zigzag']. I believe the length of this was being perceived as a value of 1. Changed the value to all_words = words.col_values(1). This returns a string data type, e.g. zigzag. This hidden_word variable now returns dashes for each individual letter of the selected word e.g. - - - - - -
    
    - Error line too long in pep8 Python validator.
        - When running an initial test within pep8 python validation, error resulted for line to long for valid_input variable. The data within this variable was a list of the letters of the alphabet to check which I was using to check against the player's guess to ensure it was a valid letter and not a number. However, due to this exceeding the 79-character limit I searched online for another solution to validify a letter input. Found a suggestion to use isalpha().
        - Initially tried changing just the value of the variable from a list of letters to isalpha(). However, when running this in the terminal received the error that isalpha() is not defined.
        - Checked online suggestion further and decided to change the if statement to a for statement and to include the isalpha() argument within this statement. Statement now states:
            - for i in guess:
                if i.isalpha():
                    print(f"you entered {guess}")
                else:
                    print(You must enter a letter)
        - When running this within the terminal the validation test was successful.
        - When entering a number, the else statement runs.
        - When entering a letter, the if statement runs.

    - display_rules() function only running once:
        - After changing the order in which the display_rules() and start_game() functions run found the display_rules() function only runs the once. If returning to home screen, entering a username again and proceeding the display_rules() function is missed and the game proceeds to start.
        - Recognised this was due to the display_rules() function being called in the main() function, and once returning to start() function it was not being called again.
        - Fixed the bug by moving the call for the display_rules() function to the end of start() function and removed from the main() function so that each time the player returns to the home screen and proceeds the display_rules function() is called.
    
    - Error of hidden word not retaining previously correct guesses.
        - Found that when running through the game, the hidden word was not retaining previously correct guesses. For example:
            - random word is guess - hidden word shows as - - - - -
            - when guessing g - the terminal will print g - - - -
            - when the player guesses another letter, e, the terminal will print - - e - -
                - The g is not retained
        - After searching online for a solution found that I needed to convert the string to a list after each guess so that it could be modified. 
        - To run this fix, I needed to track the position of the letters of the hidden word and update that position with the letter if it matched the players guess.
        - Throughout each iteration the hidden word would be converted to a list and then converted back to a string to print to the terminal.

    - Fixed error of hidden word not updating to entire correct word if correct word is guessed.
        - Whilst above error had been fixed, when testing what would happen when entering a whole word, found that the hidden word did not update, however the print statements were correct, stating the player was correct and the used words list was also updating with all the letters entered.
        - Attempted to fix this by adding an extra elif argument to the if statement to check the player is entering a letter. However this through errors up within the terminal and the game crashed.
        - After some searching for solutions online, fixed the error by changing the if statement within check_correct_answer() function.
            - Before the code runs to check if the letter is correct and updating the hidden word accourdingly, the code checks if the entery is the same as and equal to the random word, if it is it will print the entire word and the game will end. If it doesnt then it will proceed to check the letter within the elif statement and so on.

    - fixed validation error for checking if user wants to play game:
        - When entering anything by Y within this input the game would proceed regardless
        - Fixed error by creating a while statement to loop round until either Y or N is entered.
    
- __Unfixed Bugs__
 - There are no unfixed bugs within this game.

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
        - Enter your repository name and click search
        - Select connect next to your repository name
    - Click on __Deploy__

## Credits

### Content
- Words for computer to generate taken from Hangman Words - https://www.hangmanwords.com/words.
- Tutorial on how to create the hangman picture steps taken from Stack Exchange - https://codereview.stackexchange.com/questions/95997/simple-game-of-hangman
- Idea for displaying Rules as print statements taken from existing python hangman game - https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py

### Code
- API settings and Constant Variables to store information from these APIs for game to run taken from the Love Sandwiches walkthrough project.
- Code for displaying the randomly selected word from the google worksheet as a series of dashes for the length of the word taken from existing python hangman game - https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py 
- Code to check validation of player's guess taken from Stack Overflow - https://stackoverflow.com/questions/15558392/how-can-i-check-if-character-in-a-string-is-a-letter-python#:~:text=By%20using%20str.,if%20it%20is%20a%20letter. 
- Guidance on tracking attempts taken from Stack Overflow - https://stackoverflow.com/questions/23842115/how-to-tell-user-how-many-attempts-left-in-python
- Guidance for resolving PEP8 error "E128: Continuation line under indented for visual indent" taken from Stack Overflow - https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent
- Understanding and Code for updating the hidden word taken from Stack Overflow - https://stackoverflow.com/questions/67609834/how-to-replace-the-specified-dash-with-the-letter
    - This was later removed as found a better methods to update the hidden word with the correct letter. This was so I could fix numerous bugs with the hidden word not updating correctly. The guidance and code used in final deployment found from the following:
        - Existing hangman game: https://github.com/paulio11/P3-Hangman-Python-Terminal-Game/blob/main/run.py#L510
        - Stack Overflow pages: https://stackoverflow.com/questions/44307988/find-all-occurrences-of-a-character-in-a-string
    https://stackoverflow.com/questions/42565525/python-function-returning-different-list  
- The above existing hangman game also gave me the idea for how to write the code to iterate through the hangman pictures. As a string cannot be modified, I would need to store an integer within another variable, the incorrect guess would update this integer which will specify the next hangman picture in the sequence to be called.
- Guidance on string methods taken from W3Schools - https://www.w3schools.com/python/python_strings_methods.asp
- Guidance for how to build code to count down guess attempts taken from Stack Overflow - https://stackoverflow.com/questions/23842115/how-to-tell-user-how-many-attempts-left-in-python
- Guidance on how to convert a letter to a dash taken from Stack Overflow - https://stackoverflow.com/questions/61927022/how-to-convert-any-letter-into-a-dash-for-hangman-game
- Understanding of the enumerate function taken from - https://www.geeksforgeeks.org/enumerate-in-python/
- Guidance on how to collect all values from a column within a worksheet taken from https://ehmatthes.github.io/pcc_2e/beyond_pcc/extracting_from_excel/


