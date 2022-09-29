import re
import random
from timeit import repeat

def get_word():
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def green_glass_door_1():
    word = get_word()
    prev_letter = ''
    for letter in word:
        letter = letter.upper()
        if letter == prev_letter:
            return True
        prev_letter = letter
    return False

def green_glass_door_2():
    word = get_word()
    pattern = re.compile(r'(.)\1')
    return pattern.search(word)

tit1 = repeat(green_glass_door_1, number=1000, repeat=4, globals=globals())
tit2 = repeat(green_glass_door_2, number=1000, repeat=4, globals=globals())

print(tit1, tit2, sep="\n")
print(sum(tit1)/sum(tit2))
