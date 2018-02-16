import math

def polysum(n, s):
    area = (0.25*n*s*s) / (math.tan(math.pi/n))
    sum = area + (n*s) * (n*s)
    return round(sum, 4)

print(polysum(5, 7))
