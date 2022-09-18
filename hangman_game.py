from random import choice

# list of words
word_list = []
# opens a txt file that contains words

correct_letters = []
lives = 6
correct_guess = 0


def chosen_word():
    word_list = []
    with open("words.txt") as words:
        for line in words.readlines():
            word_list.append(line.rstrip('\n'))
    guess_word = choice(word_list)
    return (guess_word)



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


def loss():
    print(f'GAME OVER!! you have lost the word was {word}'.center(200))
    return True

def win():
    print(f'Congratulations!! you have guessed the correct word with {lives} lives remaining'.center(200))
    return True





word = chosen_word()
print(word)




while lives > 0 and correct_guess < len(word):
    blank_guess(word)
    user = user_guess()
    lives, correct_guess= check_user_guess(word, lives, correct_guess, user)

