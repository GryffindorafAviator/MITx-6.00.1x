# Problem 3
# 10/10 points (graded)
# Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    def abs_exp(base, exp, num):
        return abs(base ** exp - num)

    exp = 0
    diff_1 = abs_exp(base, exp, num)
    exp = 1
    diff_2 = abs_exp(base, exp, num)

    while diff_2 < diff_1:
        exp += 1
        diff_1 = diff_2
        diff_2 = abs_exp(base, exp, num)

    return exp-1




print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
