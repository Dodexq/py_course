colors = ['red', 'blue', 'green', 'orange']
new_colors = sorted(colors)
print(new_colors)

new_colors2 = sorted(colors, reverse=True)
print(new_colors2)

new_colors3 = sorted(colors, key=len)
print(new_colors3)

def get_lastname(name):
    return name.split()[-1]

people = ['George Washington', 'John Adams',
          'Thomas Jefferson', 'John Quincy Adams']
new_people = sorted(people, key=get_lastname)
print(new_people)

new_people2 = sorted(people, key=lambda name: name.split()[-1])
print(new_people2)

new_colors4 = sorted(colors, key=len, reverse=True)
print(new_colors4)