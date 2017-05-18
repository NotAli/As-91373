
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

def print_game_info(lives, guessed_letters, printed_word):
    print("You have {} lives left out of 18".format(lives))
    print("""The letters that you have guessed so far are: {} """.format(", ".join(guessed_letters)))
    print(", ".join(printed_word))  

def guess_and_check(guessed_letters, the_word, lives, printed_word):
    while True:
        try:
            current_guess = input("Please guess one letter".lower)
        except ValueError:
            current_guess = input("Your previous input wasn't valid. Please try again and enter one letter".lower)
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
            except:
                current_guess = input("I'm sorry but your input is incorrect. please only guess one letter. For example: F ")

