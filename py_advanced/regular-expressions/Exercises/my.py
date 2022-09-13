from ast import pattern
import re

def find_iter1():
    patt=re.compile("\d+")
    num_iter = patt.finditer("111 222       333 ---- 444")

    for i in num_iter:
        print(i)

def find_iter2():
    patt=re.compile("\d+")
    test_str = "111 222       333 ---- 444"
    result = re.finditer(patt, test_str)
    [print(i.group(0)) for i in result]

def main():
    find_iter1()
    print()
    find_iter2()

main()