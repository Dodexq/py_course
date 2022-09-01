def show_num(num):
    if num == 0:
        pass
    else:
        q,digit = divmod(num,10)
        show_num(q)
        print(digit,end="")

show_num(123)