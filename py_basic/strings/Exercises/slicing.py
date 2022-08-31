def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is", phrase)
    chr_start = int(input("Character to start with? "))
    chr_end = int(input("Character to end with? "))

    print("Your substring is", phrase[chr_start - 1:chr_end])

main()