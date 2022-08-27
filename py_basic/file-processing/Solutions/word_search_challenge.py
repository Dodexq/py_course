def search(word, text):
    """Return tuple holding line num and line text."""
    results = []
    for line in enumerate(text, 1):
        if line[1].find(word) >= 0:
            results.append(line)
    return results

def main():
    with open('my_files/zen_of_python.txt') as f:
        zop = f.readlines()

    word = input('Enter search word: ')
    results = search(word, zop)
    if not results:
        print(word, 'was not found.')
        
    for result in results:
        print(word, ' appears on line ', result[0],
              ': ', result[1], sep='', end='')

main()