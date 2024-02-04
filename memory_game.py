import time
import random


def list_validate_numbers(input_list):
    res = True
    valid_numbers = []
    for num in input_list:
        if num.isdigit():
            valid_numbers.append(int(num))
        else:
            print(f"Invalid values: {num}")
            print('You can write only numbers please :')
            res = False
    return res


def generate_sequence(difficulty):
    ran_list = []
    for i in range(difficulty):
        ran_num = random.randrange(1, 101)
        ran_list.append(ran_num)
    return ran_list


def get_list_from_user(difficulty):
    user_input = input(f"Please Enter a list of {difficulty} values separated by commas: ")
    user_list = user_input.split(",")
    res = list_validate_numbers(user_list)
    list_len = len(user_list)
    while res != True or list_len != difficulty:
        user_input = input(f"Please Enter a list of {difficulty} values separated by commas: ")
        user_list = user_input.split(",")
        res = list_validate_numbers(user_list)
        list_len = len(user_list)
    int_user_list = [int(i) for i in user_list]
    return int_user_list


def is_list_equal(ran_list, user_list):
    res = True
    if ran_list == user_list:
        print("Well done, YOU WIN !! your memory is excellent, you've guess the same list of numbers -:)")
        res = True
    else:
        print("Bad news, YOU LOSE !! your list of numbers doesn't match the random list, you may try again -:) \n")
        res = False
    return res


def play_memory_game(difficulty):
    print('''We are starting the Memory Game, it will be so fun :), Enjoy it.. \n 
we will show you a list of random numbers for a short time, \n you will need to try remember it.. Good luck -:)\n''')
    input('Click enter once you ready..\n')
    ran_list = generate_sequence(difficulty)
    print(ran_list, end='')
    time.sleep(1)
    for i in range(difficulty, 0, -1):
        print(i, end='\r')
    user_list = get_list_from_user(difficulty)
    if is_list_equal(ran_list, user_list):
        print(f'Random list is: {ran_list} and your list is {user_list} !!')
        res = True
    else:
        print(f'Random list is: {ran_list} and your list is {user_list} !!')
        res = False
    return res
