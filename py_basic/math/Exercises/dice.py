import random

def roll_die(sides):
    return random.randint(1, sides)

def main():
    total = 0
    sides = int(input("How many sides? "))
    
    print("You rolled a", roll := roll_die(sides))
    total += roll
    print("Total after first roll:", total)
    
    print("You rolled a", roll := roll_die(sides))
    total += roll
    print("Total after 2 roll:", total)

    print("You rolled a", roll := roll_die(sides))
    total += roll
    print("Total after 3 roll:", total)

    print("Your average roll was", total / 3)

main()