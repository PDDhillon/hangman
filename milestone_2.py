import random
word_list = ["lemon", "lime", "mango", "pineapple", "passionfruit"]
word = random.choice(word_list)
print(word)
guess = input("Please enter a single letter.")
if(len(guess) == 1 and str.isalpha(guess)):
    print("Good Guess")
else:
    print("Oops! That is not a valid input")