import random

def main():
    roshambo = ["Rock", "Paper", "Scissors"]
    choice = roshambo[int(input("1 for Rock, 2 for Paper, 3 for Scissors: ")) - 1]
    comp_choice = random.choice(roshambo)
    print(f"Computer: {comp_choice}\nUser: {choice}")

main()