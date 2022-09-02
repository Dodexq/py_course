def all_true(iterable):
    for i in iterable:
        if bool(i) == False:
            return False
    return True

def any_true(iterable):
    for i in iterable:
        if bool(i) == True:
            return True
    return False

def main():
    a = all_true([1, 0, 1, 1, 1])
    b = all_true([1, 1, 1, 1, 1])
    c = any_true([0, 0, 0, 1, 1])
    d = any_true([0, 0, 0, 0, 0])

    print(a, b, c, d) # Should be: False True True False

main()