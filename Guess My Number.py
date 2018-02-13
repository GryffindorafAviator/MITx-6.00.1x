print("Please think of a number between 0 and 100!", end='\n')

min = 0
max = 100

while True:
    ans = min + (max - min)//2

    print("Is your secret number", end=' ')
    print(ans, end='?\n')

    guess = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly.")

    if guess == 'c':
        print("Game over. Your secret number was: ", end=str(ans))
        break
    elif guess == 'h':
        max = ans
    elif guess == 'l':
        min = ans
    else:
        print("Sorry, I did not understand your input.")
