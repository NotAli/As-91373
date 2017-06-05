#Alicia Notley
#Coding started on: 16/05/17.
#Coding Finished on the:
#As 91373
#Hangman Game.

#Setting up my four functions.
def game_setup():
    word_list = ["abrubtly", "askew", "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo",
                 "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom",
                 "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow",
                 "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping",
                 "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby", "galaxy", "galvanize", "gazebo", "giaour", "gizmo",
                 "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic" , "icebox", "injury", "ivory",
                 "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging",
                 "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwifruit",
                 "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify",
                 "naphtha", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", 
                 "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quixotic", "quiz", "quizzes", "quorum",
                 "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths",
                 "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant",
                 "triphthong", "twelfth", "twelfths", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism",
                 "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy",
                 "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", 
                 "zodiac", "zombie"]
    import random
    the_word = list(random.choice(word_list))
    printed_word = [["?"]] * len(the_word)
    lives = 18
    guessed_letters = []
    return lives, the_word, printed_word, guessed_letters    

#New Function
def print_game_info(lives, guessed_letters, printed_word):
    print("You have {} lives left out of 18".format(lives))
    print("""The letters that you have guessed so far are: {} """.format(", ".join(guessed_letters)))
    print(", ".join(printed_word))  

#New Function
def guess_and_check(guessed_letters, the_word, lives, printed_word):
    current_guess = input("Please guess one letter".lower)
    if current _guess num or str?
    if len(current_guess) == 1:
        guessed_letters.append(current_guess)
        for letters in the_word:
            if current_guess in the_word:
                index = the_word.index(current_guess)
                printed_word[index] = current_guess
                print("Welldone! The letter that you have guessed is in the word.")
            else:
                lives -= 1
                print("I'm sorry but your guess is incorrect better luck next time")
    else:
        print("Sorry but your input isn't valid")
        while True:
            try:
                current_guess = input("Please guess only one letter. For example: E ".lower)
            except ValueError:
                current_guess = input("I'm sorry but your input is incorrect. please only guess one letter. For example: F ")

#New Function
def games_played(num_games, played_games):
    import sys
    import os
    while True:
        if played_games != num_games:
            print("You have requested to play {} games of hangman. So far you've completed {} games of hangman.".format(num_games, played_games))
            continue_ = input("Would you like to continue playing or would you like to quit? Press c if you would like to continue and type quit if you would like to exit the game.".lower)
            if continue_ == c:
                break
            elif continue_ == q:    
                raise SystemExit
            else:
                print("Your input isn't valid. Please try again.")
                continue_ = input("Would you like to continue playing or would you like to quit? Press c if you would like to continue and type quit if you would like to exit the game.".lower)
        else:
            while True:
                try:
                    continue_ = input("You have completed all of your requested games. If you would like to play again please press c. If you'd like to quit please press q".lower)
                    if continue_ == c:
                        break
                         python = sys.executable
                        os.execl(python, python, * sys.argv)
                    elif continue_ == q:
                        raise SystemExit
                except ValueError:
                    continue_ = input("You have completed all of your requested games. If you would like to play again please press c. If you'd like to quit please press q".lower)

#Starting the main routine.
print("Welcome to Hangman!")
while True:
    try:
        num_games = int(input("How many games of hangman would you like to play?"))
    except ValueError:
        print("I'm sorry but your input isn't valid.")
        num_games = int(input("How many games of hangman would you like to play?"))
game_setup()
played_games = 0
played_games += 1
while the_word != printed_word or lives != 18:
    print_game_info(lives, guessed_letters, printed_word)
    guess_and_check(guessed_letters, the_word, lives, printed_word)
else:
    if the_word == printed_word:
        games_played(num_games, played_games)
        print("Bad luck. You've run out of lives. The word was {} and you guessed {}".format(the_word, printed_word))
        games_played(num_games, played_games)


