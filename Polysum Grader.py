import math

def polysum(n, s):
    """A regular polygon has n number of sides. Each side has length s.

    The area of a regular polygon is: 
    The perimeter of a polygon is: length of the boundary of the polygon
    Write a function called polysum that takes 2 arguments, n and s. 
    This function should sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places."""
    
    area = (0.25*n*s*s) / (math.tan(math.pi/n))
    sum = area + (n*s) * (n*s)
    return round(sum, 4)

print(polysum(5, 7))
