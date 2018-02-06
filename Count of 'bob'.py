count = 0
countLetter = 0
lenth = len(s)

for letter in s:
    countLetter += 1
    if letter == 'b' and countLetter < lenth - 1:
        if s[countLetter] == 'o':
            if s[countLetter + 1] == 'b':
                count += 1

print('Number of times bob occurs is: ' + str(count))
