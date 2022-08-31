def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is", phrase)
    chr = int(input("Which character? "))
    
    print("Character", chr, "is",phrase[chr])

main()