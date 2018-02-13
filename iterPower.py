def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    prod = 1
    for i in range(0, exp):
        prod = prod * base
    
    return prod
