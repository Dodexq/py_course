import os

def open_state(state):
    os.chdir(os.path.dirname(__file__))
    with open('../data/states.txt') as f:
        words = [i.split() for i in (f.read().splitlines())]
    
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
        inp = input("Enter state abbr ex 'NY' q=quit: ").upper()
        if inp == "q".upper():
            break
        else:
            print(open_state(inp))
main()