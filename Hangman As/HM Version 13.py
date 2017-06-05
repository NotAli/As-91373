#Alicia Notley
#Coding started on: 16/05/17.
#Coding Finished on the: 04/06/17
#As 91373
#Hangman Game.

import random
import os

#This module sets up all of the variables and lists for the game
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
    # the chosen word is being randomly choosen from the word_list and being seperated (split) into a list using the list() function
    the_word = list(random.choice(word_list))
    #Creating the list that is going to be printed the screen and compared to the_word list
    global printed_word
    printed_word = ["___"] * len(the_word)
    #Create a list that adds all of the accepted guesses into a list so that the user can better decern their next move (better usability)
    global guessed_letters
    guessed_letters = []
    #The return enables the_word list to be accesed outside of this function and minimises the amount of global variables that I have
    return the_word

#This function prints the hangman picture as you guess the wrong letters
def print_hangman_cartoon(lives):
    #The first if statement prints the top of the gallow if they lose 1 life
    if lives < 8:
        print("-----")
        #THIS IF LOOP CONTROLS THE 2ND LINE OF THE PICTURE
        #if the lives value is equal to 0 it will print the gallows supportbeam and the head. (The final piece of the picture)
        if lives in range(0,1):
            print("|  O")
        #If the lives valuse is equal to 1 through to 6 it will print only the gallows support beam
        elif lives in range(1,7):
            print("| ")
        #else it saves the line for the picture but it doesn't actually print anything. 
        else:
            print(" ")

        #THIS IF/ELIF/ELSE LOOP CONTROLS THE 3RD LINE OF THE PICTURE
        #if lives is equal to 0-3 print the torso of the man in the gallows and the second line of the gallows support beam
        if lives in range(0,4):
            print("| /|\ ")
        #if lives equals 4 this line will print the gallow support beam, the left arm and the body
        elif lives in range(4,5):
            print("| /|")
        #if lives equals 5 it will print the gallow support beam and the left arm
        elif lives in range(5,6):
            print("| /")
        #If lives equals 6 it will only print the gallow support beam
        elif lives in range(6,7):
            print("| ")
        #Else there will be blank 'space saving' line that is printed
        else:
            print(" ")

    #THIS LOOP CONTROLS THE 4TH (LAST) LINE OF THE PICTURE
    #if lives equals 0 or 1 it will print the gallow support beam and both legs
    if lives in range(0,2):
        print("| / \ ")
    #if lives equals 2 it will print the gallow support beam and the left leg
    elif lives in range(2,3):
        print("| /")
    #if lives equals 3-6 it will print the gallow support beam
    elif lives in range(3,7):
        print("| ")
    #Else a space saving line will be printed
    else:
        print (" ")

    #After the picture has been printed the lives variable is printed out so that it is clearer to the user.
    print("LIVES = {}".format(lives))


#This function prints out the current status of the printed_word, the hangman picture and guessed_letters
def print_game_info(lives):
    print_hangman_cartoon(lives)     #This calls the other function
    guessed_letters.sort()          #This sorts the list into alphabetical order so that it is more effective to the user
    print("""The letters that you have guessed so far are: {} """.format(" ".join(guessed_letters)))
    print(" ".join(printed_word)) #The join function makes the printed list more aethstetically pleasing
    
#This function processes the users guess. It checks if it's correct, incorrect or invalid data and acts accordingly
def guess_and_check(lives, the_word):
    #To ensure that the loop won't stop until the correct input has been inputted
    while True:
        #Try loop what I want done
        try:
            #correct_letter is a counter which controls which loops the users input is cycled through.
            correct_letter = False
            #Blank line is to aid readibility in the scripting window
            print(" ")
            current_guess = input("Please guess one letter. ").lower()
            #The append() function adds data to the end of a list
            guessed_letters.append(current_guess)
            print(" ") 
            #This for loop loops through each index (letter) of the list
            for i in range(0, len(the_word)):
                #Loop starts if the users guess is the same as the current index being checked
                if current_guess == the_word[i]: 
                    #replaces the correctly identified index number of the printed_word list with the users correct guess.
                    printed_word[i] = current_guess 
                    #The change in the boolean value of the variable stops the users input from being cycled through the following loops
                    correct_letter = True
            
            #If the users guess is already on the guessed_letters list more than once
            if guessed_letters.count(current_guess) >= 2:
                print("This letter has already been guessed")
                #Save the index number of the repeated guessed letter in the variable index_num
                #Remove it from the guessed_letters list using the index_num varible
                index_num = guessed_letters.index(current_guess)
                guessed_letters.pop(index_num)
            
            #If the users guess is longer than two characters or is anything other than an alphabetic character    
            elif len(current_guess) != 1 or current_guess.isalpha() == False:
                print("Your input isn't valid. Please Try again.")
                #Save the offending index_num of the guess within list guessed_letters and remove
                index_num = guessed_letters.index(current_guess)
                guessed_letters.pop(index_num)
                #This value is set to True here, not because the correct letter has been found like the name suggests (in this one usage)
                # but because it is needed so that the program doesn't run the next elif loop but rather will skip it. 
                correct_letter = True
            
            #If the guess is wrong
            elif correct_letter == False:
                lives -= 1
                print("Your guess is incorrect.")

           #If the guess is correct. (congratulatory message)
           #This is placed here and not inside the for or nested if loop because if it was, and there are repeating 
           #letters the message would print more than once.    
            else:
                print("Your guess is correct")
            #Returns lives variable so that i can further use it inside of the program
            return lives 
            #This breaks out of the while loop
            break
        
        #If the user inputs something which breaks the loop the user will be promted to try again
        except ValueError:
            current_guess = input("Your input is invalid. Please try again. ")

#This function displays the users result and asks them if they would like to play again
def display_result(the_word, lives):
    try:
        #If the_word is the same as printed_word. (If they have won the game)
        if the_word == printed_word:
            #The join function prints out the list in an easy to read way
            print("Well Done you've won, the word was {}".format(" ".join(the_word)))
            print(" ")

        #If they lost the game.    
        else: 
            #calls the function so that the last hangman picture can be played (The full gallows. For consistency)
            lives = print_hangman_cartoon(lives)
            print("Bad luck. You've run out of lives. The word was {} and you guessed {}".format(" ".join(the_word), " ".join(printed_word)))
        
            #This value is in the try loop so that no matter whether the user wins or loses, 
        #they still get asked whether they want to play again or quit.
        continue_ = input("Would you like to play again? Type y if yes or hit any other key to quit ").lower()
        print(" ")

       #This loop accepts the users input of y and reruns the whole game
       #if the letter y is found inside of the variable continue 
        if 'y' in continue_:
            #The following statement opens a new window
            os.system("cls")
            #this function call reruns the whole game
            game_outline()
        else:
            print("Thank you for playing!")
            
    except ValueError:
        print("Sorry but your input is incorrect please try agian")

#This function runs the game and calls the other functions.
def game_outline():
    #The next statement changes the colour of the text when it is run. The colour is AQUA
    os.system("color 03")
    print("WELCOME TO VOCABULARY BUILDING HANGMAN, WHERE WE MAKE KNOWLEDGE GREAT AGIAN")
    lives = 8
    #The call statement is set to equal a value so that the changes to the list that is made within the function can be accessed 
    #Outside of the function
    the_word = game_setup()
    #While the_word isn't equal to the printed_word and lives isn't equal to 0
    while the_word != printed_word and lives != 0:
        #Calls the next to functions repeatitivly 
        print_game_info(lives)
        lives = guess_and_check(lives, the_word)
    #Calls the next two functions
    print_game_info(lives)
    display_result(the_word, lives)
  
#The main routine is below
#The following statement changes the title of the game when it is played
os.system("title Vocabulary Building Hangman")
#Calls the function which controls the whole game so that you can call the whole game at one time
game_outline()



