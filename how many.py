animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

animList = list(animals.values())
print(len(animList))
for i in range(len(animList)):
    print(i)

print(list(animals.values()))

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    animList = list(aDict.values())
    amount = 0
    for i in range(len(animList)):
        amount += len(animList[i])

    return amount

print(how_many(animals))
