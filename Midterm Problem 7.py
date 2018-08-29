# Problem 7
# 0.0/20.0 points (graded)
# Write a Python function called satisfiesF that has the specification below. 
# Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

# def satisfiesF(L):
#     """
#     Assumes L is a list of strings
#     Assume function f is already defined for you and it maps a string to a Boolean
#     Mutates L such that it contains all of the strings, s, originally in L such
#             that f(s) returns True, and no other elements. Remaining elements in L
#             should be in the same order.
#     Returns the length of L after mutation
#     """
    # Your function implementation here

# run_satisfiesF(L, satisfiesF)
# For your own testing of satisfiesF, for example, see the following test function f and test code:

# def f(s):
#     return 'a' in s
      
# L = ['a', 'b', 'a']
# print satisfiesF(L)
# print L
# Should print:

# 2
# ['a', 'a']
# Paste your entire function satisfiesF, including the definition, in the box below. 
# After you define your function, make a function call to run_satisfiesF(L, satisfiesF). 
# Do not define f or run_satisfiesF. Do not leave any debugging print statements.

def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    if len(L) == 0:
        return 0

    else:
        for item in L[:]:  #runs through copy of list so as not to skip place of char removed
            if not f(item):
                L.remove(item)

        return len(L)

run_satisfiesF(L, satisfiesF)

L = ['a', 'b', 'a']
print(satisfiesF(L))

print(L)

K = []
print(satisfiesF(K))
print(K)
