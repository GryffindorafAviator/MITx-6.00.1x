# Problem 1
# 10/10 point (graded)
# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily
# code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list
# of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord
# are in lettersGuessed) and False otherwise.

# Example Usage:
# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(isWordGuessed(secretWord, lettersGuessed))
# False

# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed1 = ['a', 'l', 'p', 'l', 'e', 's']


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
        else:
            return False

    if count == len(secretWord):
        return True
    else:
        return False

print(isWordGuessed(secretWord, lettersGuessed))
print(isWordGuessed(secretWord, lettersGuessed1))
