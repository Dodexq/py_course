import os
os.chdir(os.path.dirname(__file__))

def add_item(item):
    with open("my_files/list.txt", "a") as f:
        f.write(item+"\n")
    print(item, "was appended")

def remove_item(item):
    with open("my_files/list.txt", "r+") as f:
        list1 = f.read().splitlines()
    for i in list1:
        if i == item:
            list1.remove(i)

    with open("my_files/list.txt", "r+") as f:
        f.write('\n'.join(list1) + '\n')
            

def delete_list():
    """Deletes the entire contents of the list by opening
    list.txt for writing."""
    pass

def print_list():
    """Prints list"""
    pass

def show_instructions():
    print("""OPTIONS:
    P
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

        if choice.lower() == 'p':
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