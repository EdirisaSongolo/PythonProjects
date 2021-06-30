
import random


def number_guess():
    print('The System will try to guess a number you choose. Please provide a minimum and maximum')
    user_number = int(
        input('Enter your number below. No changing your mind\n'))
    minimum = int(input('Enter your minimum end\n'))
    maximum = int(input('Enter your maximum end\n'))

    sys_guess = random.randint(minimum, maximum)
    print(f'The system\'s initial guess is {sys_guess}')

    while sys_guess != user_number:
        print(
            f'Is {sys_guess} greater than or lower than your number \nPlease enter High or Low')
        user_response = input().lower()
        if user_response == "high":
            maximum = sys_guess-1
        elif user_response == "low":
            minimum = sys_guess + 1
        sys_guess = random.randint(minimum, maximum)
        print(f'The new number is {sys_guess}')
    else:
        print(
            f'The System has guessed your number correctly. \nBehold {sys_guess}')


number_guess()
