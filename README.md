# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


# Milestone 2
This milestone lays the foundations for the hangman game. I started by defining a list of my favourite fruits. Using python's in-built module "random", i choose a random record from this list and print to the terminal.

Next using the built in input function, I prompted the user to give me a single character. I then validated that input to make sure it was alphabetical, as well as length 1.

# Milestone 3
Building upon the code written in milestone 2, a few extra layers and abstractions were created. A new "ask_for_input" method is used to get user input. This is performed in a while loop, which is only broken when a correct input is passed. This must be a single character and alphanumeric, as in milestone 2.

A new "check_guess" function has been created to verify whether the guessed character is in fact inside of the main word, selected at the beginning. The guessed character is converted to lowercase and then checked.

# Milestone 4
Milestone 4 taught the theory and principles of Object oriented programming and the 4 main principles (Inheritance, Abstraction, Encapsulation and Polymorphism). These principles were put into use, as we abstracted and encapsulated previous functions to create a new Hangman class. 

This class now housed the functions to ask for input, as well as to check the guesses that the user inputted. On top of this, class attributes were added to facilitate a full playthrough of the game such as : number of lives, guessed letters and how much of the word is left to be guessed.

# Milestone 5
Rounding off the project, I took everything that we had iteratively created across previous milestones and collated them in my milestone_5.py file. This class was then instantiated into an object stored in my variable game. An infinite while loop was created and the game's ask for input function was called repeatedly. The only stopping mechanisms were whether the lives were == 0 OR there were no more letters to guess.

Overall, I have learnt how to utilise the fundamental concepts of python, in order to create a functioning game. As an experienced developer, the prerequisites have really helped to see some of the niche elements in python such as Mixins and Magic Methods.

Happy Gaming!