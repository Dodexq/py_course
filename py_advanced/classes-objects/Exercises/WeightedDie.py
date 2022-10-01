import random

from Die import Die

class WeightedDie(Die):
    
    def __init__(self, weights, sides=6):
        
        if len(weights) != sides:
            raise Exception(f'weights must be a list of length {sides}.')
        self._sides = sides
        self._weights = weights
        self._rolls = []
    
    def roll(self):
        options = []
        for i in range(self._sides):
            for j in range(int(self._weights[i])):
                options.append(i+1)
        roll = random.choice(options)
        self._rolls.append(roll)
        return roll

def main():
    ibj = WeightedDie([1,1,1,1,2,2])
    print(ibj.roll())

if __name__ == "__main__":
    main()