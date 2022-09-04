# ZeroDivisionError
try:
    1/0
except Exception as e:
    print(type(e))
    print(e, '\n')

# ValueError
try:
    int("a")
except Exception as e:
    print(type(e))
    print(e, '\n')

# NameError
try:
    a = b + c
except Exception as e:
    print(type(e))
    print(e, '\n')

# FileNotFoundError
try:
    open('file.txt', 'r')
except Exception as e:
    print(type(e))
    print(e, '\n')

# ImportError
try:
    import best_life
except Exception as e:
    print(type(e))
    print(e, '\n')

# TypeError
try:
    nums = [1,2,3]
    next(nums)
except Exception as e:
    print(type(e))
    print(e, '\n')

# AttributeError
try:
    greeting = "Hello Word"
    greeting.len()
except Exception as e:
    print(type(e))
    print(e, '\n')

# StopIteration
try:
    nums = [1, 2]
    iter_nums = iter(nums)
    print(next(iter_nums))
    print(next(iter_nums))
    print(next(iter_nums))
except Exception as e:
    print(type(e))
    print(e, '\n')

# KeyError
try:
    dict1 = {"1":"a","2":"b"}
    print(dict1[3])
except Exception as e:
    print(type(e))
    print(e, '\n')