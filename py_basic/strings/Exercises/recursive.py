def show_num(num):
    if num == 0:
        pass
    else:
        q,digit = divmod(num,10)
        show_num(q)
        print(digit,end="")

show_num(123)


def show_num_rever(num):
    if num == 0:
        pass
    else:
        q,digit = divmod(num,10)
        print(digit,end="")
        show_num(q)
        
print("")
show_num_rever(123)