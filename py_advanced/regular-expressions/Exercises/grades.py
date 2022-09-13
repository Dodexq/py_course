import re
import os

os.chdir(os.path.dirname(__file__))

def main():
    pattern = re.compile("subj: (.*) grades: (.*)$", re.MULTILINE)
    with open("grades.txt", "r", encoding="utf8") as f:
        for i in f:
            match_obj = pattern.match(i)
            if not match_obj:
                pass
            print(match_obj.groups(0))

main()