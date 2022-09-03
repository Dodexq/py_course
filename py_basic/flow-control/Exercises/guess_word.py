import random
import os

def get_word():
    os.chdir(os.path.dirname(__file__))
    with open('../data/words.txt') as f:
        words = f.read().splitlines()
    return random.choice(words).upper()
    
def check(word, guesses):
    status = ''  
    for w in word:
        if w in guesses:
            status += w
        else:
            status += "*"
    return status

def main():
    word = get_word() 
    n = len(word) 
    guesses = [] 
    guessed = False
    print('The word contains {} letters.'.format(n))

    while not guessed:
        guess = input('Guess a letter or a {}-letter word: '.format(n))
        guess = guess.upper()

        if len(guess) == 1:
            if guess not in guesses:
                guesses.append(guess)
            else:
                print("There is already a letter", guess)
        else: 
            print("Enter one letter or the whole word", len(word), "letter")

        if len(guess) == len(word):
            if guess == word:
                print("Yes, its", guess)
                guessed = True
                break
            else:
                print("The word is wrong", guess)
        
        if check(word, guesses) == word:
            break
        print(check(word, guesses))

    if len(guesses) == 0:
        print('{} is it! It took 1 tries.'.format(word))
    else:
        print('{} is it! It took {} tries.'.format(word, len(guesses)))

main()