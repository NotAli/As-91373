#Alicia Notley
#Coding started on: 16/05/17.
#Coding Finished on the:
#As 91373
#Hangman Game.

import random
def game_setup(): 
    word_list = ["abrubtly", "avenue", "awkward", "bagpipes", "bandwagon", "banjo", "beekeeper", "bikini", "blitz", "blizzard", 
                 "boggle", "bookworm", "buffalo", "buzzing", "cobweb", "cockiness", "croquet", "cycle", "dizzying", "dwarves",
                 "embezzle", "equip", "espionage", "exodus", "fake", "fishhook", "fixable", "flopping", "fluffiness", "flyby", 
                 "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "galaxy", "galvanize", "gazebo", "gizmo", "glowworm", 
                 "cliff", "gnarly", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "icebox", "injury", "ivory", "ivy", 
                 "jackpot", "jawbreaker", "jaywalk", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", 
                 "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", 
                 "kiwifruit", "klutz", "knapsack", "larynx", "length", "lucky", "luxury", "matrix", "megahertz", "microwave", 
                 "mystify", "nightclub", "numbskull", "onyx", "oxidise", "oxygen", "pajamas", "peekaboo", "phlegm", "pixel", 
                 "pizazz", "pneumonia", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quixotic", "quiz", "razzmatazz",
                 "rhubarb", "rhythm", "schnapps", "scratch", "sphinx", "spritz", "squawk", "staff", "strength", "stretch", "stronghold", 
                 "subway", "swivel", "syndrome", "topaz", "transcript", "unknown", "unworthy", "uptown", "vortex", "walkway", "waltz", 
                 "wave", "whomever", "wristwatch", "xylophone", "yachtsman", "yippee", "youthful", "zigzag", "zombie"]
    the_word = list(random.choice(word_list))
    global printed_word
    printed_word = ["___"] * len(the_word)
    global guessed_letters
    guessed_letters = []  
    return the_word

def print_hangman_cartoon(lives):
    if lives < 8:
        print("-----")
        if lives in range(0,1):
            print("|  O")
        elif lives in range(1,7):
            print("| ")
        else:
            print(" ")
        if lives in range(0,4):
            print("| /|\ ")
        elif lives in range(4,5):
            print("| /|")
        elif lives in range(5,6):
            print("| /")
        elif lives in range(6,7):
            print("| ")
        else:
            print(" ")
    if lives in range(0,2):
        print("| / \ ")
    elif lives in range(2,3):
        print("| /")
    elif lives in range(3,7):
        print("| ")
    else:
        print (" ")
    print("LIVES = ", lives)

def print_game_info(lives):
    print_hangman_cartoon(lives)
    print("""The letters that you have guessed so far are: {} """.format(" ".join(guessed_letters)))
    print(" ".join(printed_word))
    print(" ") 

def guess_and_check(lives, the_word):
    while True:
        try:
            correct_letter = False
            current_guess = input("Please guess one letter. ").lower()
            print(" ")  
            guessed_letters.append(current_guess)
            
            for i in range(0, len(the_word)):
                if current_guess == the_word[i]: 
                    printed_word[i] = current_guess 
                    correct_letter = True
            
            if len(current_guess) != 1 or current_guess.isalpha() == False:
                print("I'm sorry but your input isn't a valid guess. Please Try again.")
        
            elif correct_letter == False:
                lives -= 1
                print("Your guess is incorrect.")
            else:
                print("Your guess is correct")
            return lives 
            break
        
        except ValueError:
            current_guess = input("I'm sorry but your input is invalid. Please try again. ")


def display_result(the_word, lives):
    try:
        if the_word == printed_word:    
            print("Well Done you've won, the word was {}".format(the_word))
            
        else: 
            lives = print_hangman_cartoon(lives)
            print("Bad luck. You've run out of lives. The word was {} and you guessed {}".format(" ".join(the_word), " ".join(printed_word)))
        continue_ = input("Would you like to play again? Type y if yes or hit any other key to quit ").lower()

        if continue_ == 'y':
            print("""=================
                    """)
            game_outline()
        else:
            print("Thank you for playing!")
            
    except ValueError:
        print("Sorry but your input is incorrect please try agian")

def game_outline():
    print("Welcome to vocabulary building hangman! Where we make knowledge great again")
    lives = 8
    the_word = game_setup()
    while the_word != printed_word and lives != 0:
        print_game_info(lives)
        lives = guess_and_check(lives, the_word)
    print_game_info(lives)
    display_result(the_word, lives)
  

#The main routine is below          
game_outline()



