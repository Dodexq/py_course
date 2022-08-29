import math

def main():
    people = int(input("How many people are eating? "))
    slice_per_person = float(input("How many slices per person? "))
    slice_per_pie = int(input("How many slices per pie? "))

    need_pizza = math.ceil((people * slice_per_person) / slice_per_pie)
    total_pie = slice_per_pie * need_pizza
    pie_left = total_pie - (people * slice_per_person)
    
    print("You need", need_pizza, "pizzas to feed", people, "people.")
    print("There will be", pie_left, "leftover slices")

main()