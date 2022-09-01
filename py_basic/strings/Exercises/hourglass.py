def hourglass(height, ch=65):
    if height == 0:
        pass
    else:
        print("{:^8}".format(chr(ch) * height), end="\n")
        hourglass(height - 2, ch + 1)
        print("{:^8}".format(chr(ch) * height), end="\n")
        

hourglass(8)