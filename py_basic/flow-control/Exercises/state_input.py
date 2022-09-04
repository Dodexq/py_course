import os

def open_state(file_name):
    opened = 0
    while type(opened) != list:
        try: 
            os.chdir(os.path.dirname(__file__))
            with open('../data/'+file_name) as f:
                opened = [i.split() for i in (f.read().splitlines())]
        except FileNotFoundError:
            file_name = input(f"{file_name} does not exist, please enter a new name: ")
        else:
            break
    return opened
        

def return_state(state, words):
    for n, i in enumerate(words,0):
        if len(i) == 3:
            words[n][0], words[n][1] = (words[n][0] + " " + words[n][1]), words[n][2]
            del words[n][2]

    if "".join([i[0] for i in words if i[1] == state]):
        return "".join([i[0] for i in words if i[1] == state])
    else:
        return f"State {state} not found"

def main():
    while True:
        try:
            abbr_input = input("Enter state abbr ex 'NY' q=quit: ").upper()
            if abbr_input == "q".upper():
                break
            else:
                print(return_state(abbr_input, open_state("states.txt")))
        except KeyboardInterrupt:
            print("Bye!")
            break
main()