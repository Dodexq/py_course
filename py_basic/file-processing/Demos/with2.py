import os
def file_path(relative_path):
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

path_to_file = file_path("my_files/zen_of_python.txt")
with open(path_to_file) as f:
    poem = f.read()

for i, line in enumerate(poem.splitlines(), 1):
    print(f"{i}. {line}")