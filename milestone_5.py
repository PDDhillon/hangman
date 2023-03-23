import milestone_4
def play_game(word_list):
    num_lives =5
    game = milestone_4.Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You Lost!")
            break
        elif(game.num_letters > 0):
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(["lemon", "lime", "mango", "pineapple", "passionfruit"])