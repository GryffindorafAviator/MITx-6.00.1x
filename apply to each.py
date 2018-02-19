def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
      
def absoluteValue(x):
    return abs(x)
    
applyToEach(testList, absoluteValue)

def addOne(x):
    return x+1
    
applyToEach(testList, addOne)
