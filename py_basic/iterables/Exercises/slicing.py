import math

def split_list(orig_list):
    ceil = math.ceil(len(orig_list) / 2)
    list1 = orig_list[:ceil]
    list2 = orig_list[ceil:]
    return [list1, list2]

def main():
    colors = ["red", "blue", "green", "orange", "purple"]
    colors_split = split_list(colors)
    print(colors_split[0])
    print(colors_split[1])

main()