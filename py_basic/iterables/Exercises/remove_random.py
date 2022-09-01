import random

def remove_random(the_list):
    return random.choice(the_list)

def main():
    colors = ['red', 'blue', 'green', 'orange']
    colors.remove(removed_colors := remove_random(colors))
    print(f"Color {removed_colors} was removed")
    print(f"Remaining {colors}")


main()