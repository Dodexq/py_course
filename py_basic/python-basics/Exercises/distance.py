def distance(x1,y1,x2,y2):
    d2 = (x1 - x2) ** 2 + (y1-y2) ** 2
    return d2 ** 0.5

print(distance(1,1,-2,1))