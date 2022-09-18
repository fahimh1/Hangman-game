from random import choice

# list of words
word_list = []
# opens a txt file that contains words
def chosen_word():
    word_list = []
    with open("words.txt") as words:
        for line in words.readlines():
            word_list.append(line.rstrip('\n'))
    guess_word = choice(word_list)
    return (guess_word)




def blank_word(word):
    blank = ''
    for letter in word:
        blank += '_ '
    print(blank)
    return blank
correct_letters = []
incorrect_letters = []

def blank_guess(c_letter,word):
    blank = ''
    print(correct_letters)
    for letter in word:
        if letter in correct_letters:
            blank += f'{letter} '
        else:
            blank += '_ '
    print(blank)
    return blank


############# calling random word




def user_guess(word):
    correct_guess = 0
    lives = 6
    while lives > 0 and correct_guess < len(word):
        guess = input('Guess a letter ')
        if guess not in correct_letters and guess in word:
            for i in word:
                if i == guess:
                    correct_guess += 1
            correct_letters.append(guess)
            blank_guess(guess,word)
            if correct_guess == len(word):
                print(f'Congratulations!! you have guessed the correct word with {lives} lives remaining'.center(200))
        else:
            lives -= 1
            print(f'Incorrect you have {lives} lives left\n'.center(200))
            if lives < 1:
                print(f'GAME OVER!! you have lost the word was {word}'.center(200))




word = chosen_word()
blank_word(word)
user_guess(word)

