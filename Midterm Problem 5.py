# Problem 5
# 20/20 points (graded)
# Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

# This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here

    ansList = []

    for key in aDict.keys():
        if aDict[key] == target:
            ansList.append(key)

    return ansList

dictionary = {1: 1, 2: 2, 3: 3, 4: 3}
dictionary_1 = {1:1}

print(keysWithValue(dictionary, 3))
print(keysWithValue(dictionary_1, 3))
