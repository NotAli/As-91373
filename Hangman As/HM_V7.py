#Alicia Notley
#Coding started on: 16/05/17.
#Coding Finished on the:
#As 91373
#Hangman Game.

#Setting up my four functions.
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
    import random
    the_word = list(random.choice(word_list))
    global printed_word
    printed_word = ["_"] * len(the_word)
    global guessed_letters
    guessed_letters = []  
    return the_word

def print_hangman(lives):
    if lives < 8:
      print ("-----")
      
      if lives in range(0,1):
        print ("|  O")
      elif lives in range(1,7):
        print ("| ")
      else:
        print (" ")
      
      if lives in range(0,4):
        print ("| /|\ ")
      elif lives in range(4,5):
        print ("| /|")
      elif lives in range(5,6):
        print ("| /")
      elif lives in range(6,7):
        print ("| ")
      else:
        print (" ")
      
      if lives in range(0,2):
        print ("| / \ ")
      elif lives in range(2,3):
        print ("| /")
      elif lives in range(3,7):
        print ("| ")
      else:
        print (" ")
      
    print ("LIVES = ", lives)

#New Function
def print_game_info(lives):
    print_hangman(lives)
    print("""The letters that you have guessed so far are: {} """.format(", ".join(guessed_letters)))
    print(printed_word)
    print(" ")
#new function
def guess_and_check(lives, the_word):
    while True:#this loop repeats until the user inputs the correct data
        try:
            found_letter = False
            current_guess = str(input("Please guess one letter. ")).lower()
            print(" ")
            guessed_letters.append(current_guess)#adds the letter that the user guessed to the list
            for x in range(0, len(the_word)):#Supposed to loop through each different index in the list
                if current_guess == the_word[x]: #if the value that the user has guessed is in the_word
                    printed_word[x] = current_guess#substitute the correctly guessed letter into the printed_word
                    found_letter = True
            if found_letter == False:
                lives -= 1
                print("I'm sorry but your guess is incorrect better luck next time")
            else:
                print("You have guessed a letter ")
            break
        except ValueError:
            current_guess = input("I'm sorry but your input is incorrect. please only guess one letter. ")
    return lives
               
#New Function
def display_result(the_word):
    try:
        if the_word == printed_word:
            print("Well Done you've won, the word was {}".format(the_word))
            #won += 1
        else:
            print("Bad luck. You've run out of lives. The word was {} and you guessed {}".format(the_word, printed_word))
            #lost += 1 
        continue_ = input("Would you like to play again? Type y if yes ").lower()
        if continue_ == 'y':
            #print("You have won {} games and lost {} games". format(won, lost))
            main()
        else:
            print("Thank you for playing!")
            
    except ValueError:
        print("Sorry but your input is incorrect")

#Starting the main routine.
def main():
    print("Welcome to Hangman!")
    lives = 8
    the_word = game_setup()
    while the_word != printed_word and lives != 0:
        print_game_info(lives)
        lives = guess_and_check(lives, the_word)
    display_result(the_word)

            
main()
