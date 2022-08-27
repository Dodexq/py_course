import os

foo = 'my_files/foo.txt'
bar = 'my_new_files/bar.txt'

def foo2bar():
    os.renames(foo, bar)
    print('Renamed', foo, 'to', bar)

def bar2foo():
    os.renames(bar, foo)
    print('Renamed', bar, 'to', foo)

foo2bar()