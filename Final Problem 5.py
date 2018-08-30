# Problem 5
# 20/20 points (graded)
# You are given a dictionary aDict that maps integer keys to integer values. 
# Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in aDict.

# This function takes in a dictionary and returns a list.
# Return the list of keys in increasing order.
# If aDict does not contain any values appearing exactly once, return an empty list.
# If aDict is empty, return an empty list.
# For example:
# If aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0} then your function should return [1, 3, 8]
# If aDict = {1: 1, 2: 1, 3: 1} then your function should return []

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    keyList = []
    keyDict = {}

    for key in list(aDict.keys()):
        if aDict[key] not in keyDict:
            keyDict[aDict[key]] = 1

        else:
            keyDict[aDict[key]] += 1

    for keyInkeyDict in keyDict.keys():
        if keyDict[keyInkeyDict] == 1:
            for keyInaDict in aDict.keys():
                if aDict[keyInaDict] == keyInkeyDict:
                    keyList.append(keyInaDict)

    print(keyDict)


    return sorted(keyList)

aDict = {1: 1, 2: 1, 3: 1}

print(uniqueValues(aDict))
