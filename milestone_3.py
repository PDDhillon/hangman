while True:
    guess = input("Please enter a single letter.")
    if(len(guess) == 1 and str.isalpha(guess)):
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")