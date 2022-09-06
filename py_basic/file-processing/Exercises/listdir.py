import os
os.chdir(os.path.dirname(__file__))

for file in os.listdir():
    if file.endswith(".py"):
        print(file)