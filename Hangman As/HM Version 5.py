#Alicia Notley
#Coding started on: 16/05/17.
#Coding Finished on the:
#As 91373
#Hangman Game.

#global lives
#Setting up my four functions.
def game_setup():
    word_list = ["zombie"]
    import random
    global the_word
    the_word = list(random.choice(word_list))
    global printed_word
    printed_word = ["_"] * len(the_word)
        #lives = int(8)
    global guessed_letters
    guessed_letters = []  

#New Function
def print_game_info():
    global lives
    print("You have {} lives left out of 8".format(lives))
    print("""The letters that you have guessed so far are: {} """.format(", ".join(guessed_letters)))
    print(printed_word)
    print(" ")

#new function
def guess_and_check():
    global lives
    while True:#this loop repeats until the user inputs the correct data
        try:
            found_letter = False
            current_guess = str(input("Please guess one letter. ")).lower()
            guessed_letters.append(current_guess)#adds the letter that the user guessed to the list
            for i in the_word:#Supposed to loop through each different index in the list
                if current_guess in the_word: #if the value that the user has guessed is in the_word
                    index = the_word.index(current_guess)#record the index number of user's guess in variable
                    printed_word[index] = current_guess#substitute the correctly guessed letter into the printed_word
                    found_letter = True
                    break
            if found_letter == False:
                lives -= 1
                print("I'm sorry but your guess is incorrect better luck next time")
            else:
                print("You have guessed a letter ")
            break
        except ValueError:
            current_guess = input("I'm sorry but your input is incorrect. please only guess one letter. ")    

#New Function
def games_played(played_games):
    print("You have requested to play {} games of hangman. So far you've completed {} games of hangman.".format(num_games, played_games))
    while played_games:
        try:
            continue_ = input("Would you like to continue playing or would you like to quit? Press c if you would like to continue and type quit if you would like to exit the game.").lower()
            if continue_ == c:
                break
            elif continue_ == q:    
                raise SystemExit
            else:
                print("Your input isn't valid. Please try again.")
                continue_ = input("Would you like to continue playing or would you like to quit? Press c if you would like to continue and type quit if you would like to exit the game.".lower)
        except ValueError:
            continue_ = input("You have completed all of your requested games. If you would like to play again please press c. If you'd like to quit please press q".lower)

#Starting the main routine.

print("Welcome to Hangman!")
global lives
lives = 8
game_setup()
played_games = 1
while the_word != printed_word and lives != 0:
    print_game_info()
    guess_and_check()

if the_word == printed_word or lives == 0:
    games_played(num_games, played_games)
    print("Bad luck. You've run out of lives. The word was {} and you guessed {}".format(the_word, printed_word))
    
