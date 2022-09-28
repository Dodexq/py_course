# %% 
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person("{self.name}",{self.age})' 
    def __str__(self):
        return f"Персона по имени {self.name} имеет возраст {self.age}"
    def say_hello(self):
        print(self.name, "Hello!")

man1 = Person(name="Artem", age=27)
man2 = Person(name="Nataly", age=29)
man3 = Person(name="Alex", age=14)
# %%
people = [man1, man2, man3]

# %%
print(people)
# %%
man1.say_hello()
# %%
print(sorted([p for p in people if p.age >= 21], 
key=lambda p: p.name))
# %%
class Employee (Person):
    def __init__(self, name, age, salary, job):
        super().__init__(name, age)
        self.salary = salary
        self.job = job

    def __str__(self):
        return super().__str__() + f" Зарплата {self.salary}, работает {self.job}"
# %%
emp1 = Employee("Vasily", 26, 150000, "Instructor")
# %%
print(emp1)
# %%
people.append(emp1)
# %%
print(sorted([p for p in people if p.age >= 21], 
key=lambda p: p.name))
# %%
