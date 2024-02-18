import random
import requests


def get_money_interval(ran_num):
    base_currency = 'USD'
    target_currency = 'ILS'
    api_url = f'https://open.er-api.com/v6/latest/{base_currency}'
    response = requests.get(api_url)
    data = response.json()
    exchange_rate = data['rates'][target_currency]
    correct_value = exchange_rate * ran_num
    return correct_value


def get_user_guess(ran_num):
    res = True
    user_guess = 1
    while res:
        user_guess = input(f'Please guess how much {ran_num} Dollars are worth in Israeli Shekel ?\n')
        try:
            int(user_guess)
            res = False
        except:
            res = True
            print('Wrong value !! you must insert only numbers, thanks')
    return float(user_guess)


def compare_results(user_guess, correct_value, game_level):
    res = True
    valid_range = 10 - game_level
    if user_guess - valid_range <= correct_value <= user_guess + valid_range:
        res = True
    else:
        res = False
    return res


def play_currency_roulette_game(difficulty):
    print('''We are starting the Currency Roulette Game, it will be so fun :), Enjoy it.. \n 
game is to guess how much random value in Dollar is worth in Israeli Shekel, \n try to be as close as possible.. Good luck -:)\n''')
    random_num = random.randrange(1, 100)
    correct_value = get_money_interval(random_num)
    user_guess = get_user_guess(random_num)
    res = compare_results(user_guess, correct_value, int(difficulty))
    if res:
        print(
            f"Well done !! you win the game, you've succeeded to guess a number: {user_guess} close enough to the correct value {correct_value}")
        res = True
    else:
        print(
            f'You Lose !! your guess : {user_guess} is too far from correct values {correct_value}, you may try again -:)')
        res = False
    return res

