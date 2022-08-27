with open('my_files/zen_of_python.txt') as f:
    poem = f.read()

# The file is now closed, but we saved its content in the poem variable
for i, line in enumerate(poem.splitlines(), 1):
    print(f"{i}. {line}")