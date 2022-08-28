def fopen():
    f = open("python-basics/Demos/my-file.txt")
    content = f.read()
    print(content)
    f.close

def fwith():
    with open("python-basics/Demos/my-file.txt", "w") as f:
        f.write(input("What you want read in file? "))

def main():
    fwith()
    fopen()

main()