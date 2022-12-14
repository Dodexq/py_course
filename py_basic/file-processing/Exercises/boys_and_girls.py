import os

def file_path(relative_path):
    folder = os.path.dirname(os.path.abspath(__file__))
    path_parts = relative_path.split("/")
    new_path = os.path.join(folder, *path_parts)
    return new_path

def file_to_list(path):
    with open(file_path(path)) as f:
        lines = f.read().splitlines()
    return lines

def subtract_lists(list1, list2):
    return [x for x in list1 if x not in list2]

def dups(list1, list2, sort=True):
    dup_list = []
    for item in list1:
        if item in list2:
            dup_list.append(item)
    if sort:
        dup_list.sort()
    return dup_list

def list_to_file(path, the_list):
    content = "\n".join(the_list)
    with open(file_path(path), "w") as f:
        f.write(content)


def main():
    boys_2018_path = "../data/2018-boys.txt"
    girls_2018_path = "../data/2018-girls.txt"
    boys_1880_path = "../data/1880-boys.txt"
    girls_1880_path = "../data/1880-girls.txt"

    boys_2018 = file_to_list(boys_2018_path)
    girls_2018 = file_to_list(girls_2018_path)
    boys_1880 = file_to_list(boys_1880_path)
    girls_1880 = file_to_list(girls_1880_path)

    boys_only_2018 = subtract_lists(boys_2018, girls_2018)
    girls_only_2018 = subtract_lists(girls_2018, boys_2018)
    boys_only_1880 = subtract_lists(boys_1880, girls_1880)
    girls_only_1880 = subtract_lists(girls_1880, boys_1880)

    boys_names_2_girls_names = dups(girls_only_2018, boys_only_1880)
    girls_names_2_boys_names = dups(boys_only_2018, girls_only_1880)

    list_to_file("../data/girls-names-that-were-boys-names.txt",
                 boys_names_2_girls_names)
    list_to_file("../data/boys-names-that-were-girls-names.txt",
                 girls_names_2_boys_names)

main()