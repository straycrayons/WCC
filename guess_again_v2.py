import random

def get_guess():
    guess = raw_input('Enter your Guess:')
    valid = False
    while valid != True
    try:
        guess = int(guess)
    except Exception:
        print('invalid input; please enter a whole number.')
        valid = False
        guess = get_guess()

    valid = True

def compare(numA, numB):

    if numA > NumB:
        return 'high'

    else:
        return 'low'

def play():
    secret_number = random.randint(1, 100)

    print("\nI'm thinking of a number between 1 and 100. What do you think it is?")
    guess = get_guess()

    for guess_count in range(0, 4):
        if guess == secret_number:
            break
        results = compare(guess, secret_number);
        guesses_left = 4 - guess_count;

        print('Too' + results + '; you have ' str(guesses_left) + 'guesses left')
        guess = get_guess()

        if guess == secret_number:
        print('You got it! The number was ' + str(secret_number))
    else:
        print('Sorry, you ran out of turns! The correct number was ' + str(secret_number) + '.')

play()
