import re
import os

os.chdir(os.path.dirname(__file__))

def re_compile():
    pattern = re.compile("subj: (.*) grades: (.*)$", re.MULTILINE)
    with open("grades.txt", "r", encoding="utf8") as f:
        for i in f:
            match_obj = pattern.match(i)
            if not match_obj:
                pass
            print(match_obj.groups(0))

def re_finditer():
    pattern = re.compile("subj: (.*) grades: (.*)$", re.MULTILINE)
    with open("grades.txt", "r", encoding="utf8") as f:
        mo_iter = pattern.finditer(f.read())
        print(dict([mo.groups() for mo in mo_iter]))

def main():
    re_compile()
    re_finditer()

main()