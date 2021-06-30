
import random


def number_guess():
    print('Enter a number below between 1 and 10')
    random_number = random.randint(1, 10)
    guess = int(input())

    while guess != random_number:
        if guess > random_number:
            print(f'{guess} is greater than the answer')
            guess = int(input())
        elif guess < random_number:
            print(f'{guess} is less than the answer')
            guess = int(input())
    else:
        print(f'You have correctly guessed the random number {random_number}')


number_guess()
