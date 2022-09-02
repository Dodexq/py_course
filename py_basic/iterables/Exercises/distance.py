import math

def distance(x1,y1,x2,y2):
    return math.hypot((x1-x2),(y1-y2))

p1 = (1,3)
p2 = (2,5)

print(distance(p1[0],p1[1],p2[0],p2[1]))
print(distance(*p1,*p2))

