#define the simple_divide function here
def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return [0 for x in range(len(item))]    
