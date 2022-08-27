with open('my_files/yoda.txt', 'a+') as f:
    f.write('Powerful you have become.')
    f.seek(0)
    print(f.read())