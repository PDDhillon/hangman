import random
word_list = ["lemon", "lime", "mango", "pineapple", "passionfruit"]
word = random.choice(word_list)
print(word)
while True:
    guess = input("Please enter a single letter")
    if(len(guess) == 1 and str.isalpha(guess)):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")