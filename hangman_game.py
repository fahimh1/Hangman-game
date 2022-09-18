from random import choice

# list of words
word_list = []
# opens a txt file that contains words

correct_letters = []
# the users correct guesses are stored in a list
lives = 6
# the amount of attempt the user has is 6
correct_guess = 0
# the number of correct guesses are stored in the variable

def chosen_word():
    word_list = []
    with open("words.txt") as words:
        for line in words.readlines():
            word_list.append(line.rstrip('\n'))
    guess_word = choice(word_list)
    return (guess_word)
# This function get words for a txt file which is then stored in a list. Then a random word is chosen from the list and
#is returned


def blank_guess(word, user_letter=0):
    blank = ''
    print(correct_letters)
    for letter in word:
        if letter in correct_letters:
            blank += f'{letter} '
        else:
            blank += '_ '
    print(blank)
    return blank
# This function creates a blank board for the word by comparing if the letters in the correct letters list

def user_guess():
    user_letter =''
    is_valid = False
    while not is_valid:
        user_letter = input('Guess a letter ')
        if user_letter.isalpha() and len(user_letter) == 1:
            is_valid = True
        else:
            print('You have not entered a valid letter :/')
    return user_letter
# This function takes the user input as a guess making sure it is in the alphabet

def check_user_guess(word,lives,correct_guess,guess):
    if guess not in correct_letters and guess in word:
        for i in word:
            if i == guess:
                correct_guess += 1
        correct_letters.append(guess)
        if correct_guess == len(word):
            win()
    else:
        lives -= 1
        print(f'Incorrect you have {lives} lives left\n'.center(200))
        if lives < 1:
            loss()
    return lives, correct_guess
# This function checks if the user's guess is correct if it is correct it adds the guess to the correct letter list
# If the guesses is incorrect then the user loses a life

def loss():
    print(f'GAME OVER!! you have lost the word was {word}'.center(200))
    return True
# Print a message stating the user guessed the word correctly

def win():
    print(f'Congratulations!! you have guessed the correct word with {lives} lives remaining'.center(200))
    return True
# Prints a message stating the user has not guessed the word correctly




word = chosen_word()
# call the function and stores it in the variable word





while lives > 0 and correct_guess < len(word):
    blank_guess(word)
    user = user_guess()
    lives, correct_guess= check_user_guess(word, lives, correct_guess, user)

