print("Please think of a number between 0 and 100!")
guess = 50
i = 2
while True:
    print("Is your secret number", end=' ')
    print(guess, end='')
    print('?')
    judge = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if i<7:
        if judge == 'h':
            guess = guess - int(100/(2**i))
            i += 1
        elif judge == 'l':
            guess = guess + int(100/(2**i))
            i += 1
        elif judge == 'c':
            print("Game over. Your secret number was:", end=' ')
            print(guess)
            break
        else:
            print("Sorry, I did not understand your input.")
    elif i==7:
        if judge == 'h':
            guess = guess - 1
            i += 1
        elif judge == 'l':
            guess = guess + 1
            i += 1
        elif judge == 'c':
            print("Game over. Your secret number was:", end=' ')
            print(guess)
            break
        else:
            print("Sorry, I did not understand your input.")
