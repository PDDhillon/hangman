import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in range(0,len(self.word))]
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter")
            if(not(len(guess) == 1 and str.isalpha(guess))):
                print("Invalid letter. Please enter a single alphabetical character")
            elif(guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
        
    
    #def test(self):
        #print(self.word, self.word_guessed, self.num_letters, self.word_list, self.list_of_guesses, self.num_lives)

test = Hangman(["lemon", "lime", "mango", "pineapple", "passionfruit"],1)
test.ask_for_input()