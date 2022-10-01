import random
from collections import Counter

class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_method(self):
        self.rolled =  random.randint(1, self.sides)
        return self.rolled

    def __str__(self):
        return f"Number {self.rolled}"

def main():
    die1 = Die()
    roll_list = [die1.roll_method() for _ in range(10000)]
    count = Counter(roll_list)
    print(count)

if __name__ == "__main__":
    main()