# Import random function to ultimately choose a word from the list
import random


# Open the list from the tree
f = open('word_list.txt', 'r')

# Separate each word in the list to individual strings
word_list = f.read().split()
# print(word_list) appears multiple times as a comment, this is to allow any debugging necessary

# Choose a word randomly from the word list
the_word = random.choice(word_list)
# print(the_word)

# define the function hangman which is what will run the game

def hangman(the_word):
    # displayed_word will be the word as the gamer will see it (initially all *s)
    displayed_word = "*" * len(the_word)
    # already_tried will be the list of letters already tried so that there are no repeats
    already_tried = []
    # correct is a boolean which will change to being True when the word is fully guessed
    correct = False
    lives = 7

# The while loop will keep the game running until there are no more lives or the word is correct
    while lives > 0 and not correct:
        # show the gamer their lives and the word as they currently have it
        print("You have " + str(lives) + " lives remaining.")
        print(displayed_word)

        # allow the gamer to guess a letter
        guess = input("Please enter your next guess: ").lower()
        print("\n")
        print("\n")
        # confirm that the gamer has only tried one letter, otherwise reject it.
        if len(guess) == 1:

            # rejects letters already guessed without penalising lives
            if guess in already_tried:
                print("This letter has already been guessed.")
                print("\n")

                # rejects letters not in the word, penalises lives, and adds the letter to the list already tried
            elif guess not in the_word:
                print("Unlucky, this letter is not in the word. You have lost a life.")
                print("\n")
                already_tried.append(guess)
                lives -= 1

                # accepts the letter
            else:
                print(guess + " was in the word")
                print("\n")
                already_tried.append(guess)
                # create a list that allows the recognition of the letter and the replacement of the *
                letters_of_word = list(displayed_word)
                count = [i for i, letter in enumerate(the_word) if letter == guess]
                for place in count:
                    letters_of_word[place] = guess
                    displayed_word = "".join(letters_of_word)

                    # allows the game to end if the word is guessed
                if "*" not in displayed_word:
                    correct = True

        else:
            print("Please only guess one letter at a time.")

    # Ends the game either with a victory or with a loss when the while loop is broken.
    if correct:
        print("The word was " + displayed_word.upper())
        print("congratulations you win")
    else:
        print("The word was " + the_word.upper())
        print("you lose")

# Runs the defined loop above. This is the only executable in the script
hangman(the_word)
