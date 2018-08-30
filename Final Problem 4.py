# Problem 4
# 15/15 points (graded)
# Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, 
# sorted in increasing order. A prime number is a number that is divisible only by 1 and itself. 
# This function takes in an integer and returns a list of integers.

def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    primesList = []

    for i in range(2, N+1):
        isPrime = True

        for j in range(2, i):
            if i%j == 0:
                isPrime = False
                break

        if isPrime:
            primesList.append(i)

    return primesList
