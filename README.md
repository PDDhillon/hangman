# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


# Milestone 2
This milestone lays the foundations for the hangman game. I started by defining a list of my favourite fruits. Using python's in-built module "random", i choose a random record from this list and print to the terminal.

Next using the built in input function, I prompted the user to give me a single character. I then validated that input to make sure it was alphabetical, as well as length 1.

# Milestone 3
Building upon the code written in milestone 2, a few extra layers and abstractions were created. A new "ask_for_input" method is used to get user input. This is performed in a while loop, which is only broken when a correct input is passed. This must be a single character and alphanumeric, as in milestone 2.

A new "check_guess" function has been created to verify whether the guessed character is in fact inside of the main word, selected at the beginning. The guessed character is converted to lowercase and then checked.