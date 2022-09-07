import os
from pprint import pp
os.chdir(os.path.dirname(__file__))

def main():
    class_stud_dict = {}
    with open("my_files/classname.txt", encoding="utf8") as f:
        for line in f:
            stud_name, ed_class = line.split()
            if ed_class in class_stud_dict:
                class_stud_dict[ed_class].append(stud_name)
            else:
                class_stud_dict[ed_class] = [stud_name]
    pp(class_stud_dict)

main()