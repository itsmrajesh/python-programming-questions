import math


def area(r):
    return math.pi*r**2


radii=[2,3,7.25,22,10]

lst=list(map(area,radii))


#map(function,iteratable)

print(lst)
