import os
os.chdir(os.path.dirname(__file__))

def add_item(item):
    with open("my_files/list.txt", "a") as f:
        f.write(item+"\n")
    print(item, "was appended")

def remove_item(item):
    item_found = False
    with open('my_files/list.txt', 'r') as f:
        items = f.read().splitlines()
        if item in items:
            items.remove(item)
            item_found = True
        else:
            print(item + ' not found in list.')

    if item_found:
        with open('my_files/list.txt', 'w') as f:
            f.write('\n'.join(items) + '\n')
        print(item, "was remove from list")

def delete_list():
    with open('my_files/list.txt', 'w') as f:
        print('List has been deleted.')

def print_list():
    with open('my_files/list.txt', 'r') as f:
        print(f.read())

def show_instructions():
    print("""OPTIONS:
    cat
        -- Print List
    +abc
        -- Add 'abc' to list
    -abc
        -- Remove 'abc' from list
    --all
        -- Delete entire list
    Q
        -- Quit\n""")

def main():
    show_instructions()

    while True:
        choice = input('>> ')

        if choice.lower() == 'q':
            print('Goodbye!')
            break

        if choice.lower() == 'cat':
            print_list()
        elif choice.lower() == '--all':
            delete_list()
        elif choice and choice[0] == '+':
            add_item(choice[1:])
        elif choice and choice[0] == '-':
            remove_item(choice[1:])
        else:
            print("I didn't understand.")
            show_instructions()

if __name__ == '__main__':
    main()