import random

def get_word():
    """Returns random word."""
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def check(word, guesses):
    """Creates and returns string representation of word
    displaying asterisks for letters not yet guessed."""
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
            print("Enter one letter or the whole word", len(word))

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

    print('{} is it! It took {} tries.'.format(word, len(guesses)))

main()