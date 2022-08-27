def search(word, text):
    """Return tuple holding line num and line text."""
    for line in enumerate(text, 1):
        if line[1].find(word) >= 0:
            return line
    return None

def main():
    with open('my_files/zen_of_python.txt') as f:
        zop = f.readlines()

    word = input('Enter search word: ')
    result = search(word, zop)
    if result:
        print(word, ' first appears on line ',
              result[0], ': ', result[1], sep='')
    else:
        print(word, 'was not found.')

main()