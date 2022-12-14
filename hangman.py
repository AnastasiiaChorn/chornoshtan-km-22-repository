# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter not in letters_guessed:
        return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    output = ""

    for letter in secret_word:
      if letter in letters_guessed:
        output += letter
      else:
        output += "_ "

    return output


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    available_letters = ""

    for letter in all_letters:
      if letter not in letters_guessed:
        available_letters += letter

    return available_letters


def warnings_count(problem_message, guessed_word, warnings_remaining, guesses_remaining):
  '''
  problem_message: string, the reason the user loses a warning or a guess
  guessed_word: string, the word that the user had to guess
  warnings_remaining: integer, the amount of warnings the user has so far (initial amount - 3)
  guesses_remaining: integer, the amount of guesses the user has so far (initial amount - 6)

  Returns: string, the message with the amount of warnings left or the message with the amount 
    of guesses left (in case all warnings are used)
  '''
  if warnings_remaining == 0:
    warnings_remaining = 3
    guesses_remaining -= 1

    if guesses_remaining > 0:
      print(f"Oops! {problem_message} You have no warnings left so you lose one guess: {guessed_word}")

  else:
    warnings_remaining -= 1
    print(f"Oops! {problem_message} You have {warnings_remaining} warnings left: {guessed_word}")

  return(warnings_remaining, guesses_remaining)


def welcome_message(secret_word, warnings_remaining):
  '''
  secret_word: string, the word to guess
  warnings_remaining: integer, the initial amount of warnings the user has

  Returns: string, the welcome messages that show the game is starting, messages 
    contain the length of the word to guess and the amount of warnings the user has
  '''
  print("Welcome to the game Hangman!")
  print(f"I am thinking of a word that is {len(secret_word)} letters long.")
  print(f"You have {warnings_remaining} warnings left.")
  print("-"*13)


def unique_letters(word):
  '''
  word: string, guessed word

  Returns: integer, the amount of unique letters in the guessed word
  '''
  return len(set(word))


def lost_guesses(letter):
  '''
  letter: string, the letter the user enters during a game

  Returns: integer, the user loses two guesses in case the entered letter is not 
    in a word and is a vowel; and one guess in case the entered letter is not in a word and is a consonant
  '''
  if letter in ["a", "e", "i", "o", "u"]:
    return 2
  else:
    return 1
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    valid_letters = string.ascii_lowercase
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []

    welcome_message(secret_word, warnings_remaining)

    while True:
      print(f"You have {guesses_remaining} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      input_letter = input("Please guess a letter: ").lower()

      guessed_word = get_guessed_word(secret_word, letters_guessed)

      if input_letter not in valid_letters:
          warnings_remaining, guesses_remaining = warnings_count("That is not a valid letter.", guessed_word, warnings_remaining, guesses_remaining)  

      elif input_letter in letters_guessed:
          warnings_remaining, guesses_remaining = warnings_count("You've already guessed that letter.", guessed_word, warnings_remaining, guesses_remaining)  

      elif input_letter in secret_word:
        letters_guessed.append(input_letter)
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

      else:
        guesses_remaining -= lost_guesses(input_letter)
        letters_guessed.append(input_letter)
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

      print("-"*13)

      if is_word_guessed(secret_word, letters_guessed):
        score = guesses_remaining * unique_letters(secret_word)
        print(f"Congratulations, you won! Your total score for this game is: {score}")
        break

      elif guesses_remaining <= 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(" ", "")
    if len(my_word) == len(other_word):
      set_letters = set(my_word.replace("_", ""))
      for letter in set_letters:
        if my_word.count(letter) != other_word.count(letter):
          return False
      for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
          return False

      return True

    else:
      return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = 0
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matches += 1
        print(word, end = " ")
    if matches == 0:
      print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    valid_letters = string.ascii_lowercase
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []

    welcome_message(secret_word, warnings_remaining)

    while True:
      print(f"You have {guesses_remaining} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      input_letter = input("Please guess a letter: ").lower()

      guessed_word = get_guessed_word(secret_word, letters_guessed)

      if input_letter == "*":
        print("Possible word matches are: ", end = "")
        show_possible_matches(guessed_word)
        print()

      elif input_letter not in valid_letters:
          warnings_remaining, guesses_remaining = warnings_count("That is not a valid letter.", guessed_word, warnings_remaining, guesses_remaining)  

      elif input_letter in letters_guessed:
          warnings_remaining, guesses_remaining = warnings_count("You've already guessed that letter.", guessed_word, warnings_remaining, guesses_remaining)  

      elif input_letter in secret_word:
        letters_guessed.append(input_letter)
        print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

      else:
        guesses_remaining -= lost_guesses(input_letter)
        letters_guessed.append(input_letter)
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")

      print("-"*13)

      if is_word_guessed(secret_word, letters_guessed):
        score = guesses_remaining * unique_letters(secret_word)
        print(f"Congratulations, you won! Your total score for this game is: {score}")
        break

      elif guesses_remaining <= 0:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
        break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
