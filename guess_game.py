import random


def input_validation(choose_num, range_numbers):
    if isinstance(choose_num, str):
        print('Invalid, you can enter only numbers!')
        return True
    elif choose_num < 1 or choose_num > range_numbers:
        print(f'Invalid, numbers must be between 0 to {range_numbers}')
        return True
    else:
        return False


def generate_number(difficulty):
    return random.randrange(1, difficulty)


def get_guess_from_user(difficulty):
    user_guess = input(f'Can you guess a number between 0 to {difficulty} please \n')
    return user_guess


def guess_compare_results(ran_num, user_guess):
    if ran_num == user_guess:
        return True
    else:
        return False


def play_guess_game(difficulty):
    print('We are starting the Guess Game, it will be so fun :), Enjoy it.. \n')
    ran_num = generate_number(difficulty)
    res = True
    user_guess = 0
    while res:
        user_guess = get_guess_from_user(difficulty)
        if user_guess.isnumeric():
            res = input_validation(int(user_guess), difficulty)
        else:
            res = input_validation(user_guess, difficulty)
    if guess_compare_results(ran_num, int(user_guess)):
        print('Well done, You win the Guess Game, your number was match to ours :) \n')
        print(f'Random number is : {ran_num} and Your number is : {user_guess}')
        res = True
    else:
        print('Wrong, your number is not match ours, please play again :)')
        print(f'Random number is : {ran_num} and Your number is : {user_guess}')
        res = False
    return res
