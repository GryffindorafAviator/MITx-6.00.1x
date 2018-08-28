# Problem 3

# (15/15 points)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if
# s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we
# suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and
# cleared your head.

# Paste your code into this box 
sub_s = s[0]
sub_s1 = ""

for i in range(len(s)):
    if i < len(s)-1:
        if s[i+1] >= s[i]:
            sub_s += s[i+1]

        else:
            if len(sub_s) > len(sub_s1):
                sub_s1 = sub_s
                sub_s = s[i+1]

            else:
                sub_s = s[i+1]

    else:
        if len(sub_s) > len(sub_s1):
            sub_s1 = sub_s

print("Longest substring in alphabetical order is:", sub_s1)
