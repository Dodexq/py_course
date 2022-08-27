import os

os.mkdir("my_files/a")
os.makedirs("my_files/a/b/c")

with open('my_files/a/a-demo.txt', 'w') as f:
    f.write('Dummy text')
with open('my_files/a/b/b-demo.txt', 'w') as f:
    f.write('Dummy text')