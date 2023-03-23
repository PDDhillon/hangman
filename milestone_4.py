import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for x in range(0,len(self.word))]
        self.num_letters = len(set(self.word))
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
    
    #def test(self):
        #print(self.word, self.word_guessed, self.num_letters, self.word_list, self.list_of_guesses, self.num_lives)

#test = Hangman(["lemon", "lime", "mango", "pineapple", "passionfruit"],1)
#test.test()