import os
os.chdir(os.path.dirname(__file__))

with open('my_files/yoda.txt', 'a+') as f:
    f.write('Powerful you have become.\n')
    f.write('Hello, Word!')
    f.seek(0)
    print(f.read())