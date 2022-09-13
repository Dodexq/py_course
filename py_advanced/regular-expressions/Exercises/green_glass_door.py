import re

def green_glass_door(word):
    exp = re.compile(r"(.)\1")
    return re.search(exp, word)

fruits = ['banana', 'apple', 'pear', 'grape', 'cherry',
          'persimmons', 'orange', 'passion fruit']

for fruit in fruits:
    if green_glass_door(fruit):
        print(f'YES! {fruit} can pass through the green glass door.')
    else:
        print(f'NO! {fruit} cannot pass through the green glass door.')