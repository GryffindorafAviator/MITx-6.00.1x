# Problem 4
# 15/15 points (graded)
# Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. 
# For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

#This function takes in a list of strings and returns a list of strings. Your function should not modify aList.

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here

    newList = []

    for str in aList:
        if len(str) < 4:
            newList.append(str)

    return newList

aList = ["apple", "cat", "dog", "banana"]

print(lessThan4(aList))
