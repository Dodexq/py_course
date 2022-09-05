import os

def search(word, text):
    result = []
    [result.append(lines) for lines in enumerate(text, 1) if word in lines[1]]
    return result 

def main():
    os.chdir(os.path.dirname(__file__))
    with open("my_files/zen_of_python.txt") as f:
        zop = f.read().splitlines()[4:]
    
    word = input('Enter search word: ')
    result = search(word, zop)
    [print(word, ' appears on line ', i[0], ': ', i[1], sep='') for i in result]\
         if result else print(word, 'was not found.')

main()