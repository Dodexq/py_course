from collections import Counter
import os

os.chdir(os.path.dirname(__file__))

with open('Declaration_of_Independence.txt') as f:
    list = f.read()

word_list = [word for word in list.upper().split() if len(word) > 5]
    
c = Counter(word_list)
print(c.most_common(10))