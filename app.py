from guess_game import play_guess_game, input_validation
from currency_roulette_game import play_currency_roulette_game
from guess_game import play_guess_game, input_validation
from main_score import score_server, insert_text_to_file
from memory_game import play_memory_game, get_list_from_user
from score import add_score
from utils import screen_cleaner
from flask_score import app


def list_validate_length(user_list, difficulty):
    while len(user_list) != difficulty:
        print(f'please enter only {difficulty} amount of values :')
        user_list = get_list_from_user(difficulty)
    res = True
    return res


def welcome():
    screen_cleaner()
    username = input('Hello, please enter your name: \n')
    print(f'Hi {username} and welcome to the World of Games: The Epic Journey \n')


def start_play():
    print('''Please chose one of the following games by clicking 1, 2 or 3: \n
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.')
    2. Guess Game - guess a number and see if you chose like the computer.')
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n''')
    res = True
    while res:
        game_num = input()
        if game_num.isnumeric():
            res = input_validation(int(game_num), 3)
        else:
            res = input_validation(game_num, 3)
    print('Thanks :) \nPlease chose now the game level you wish to play, between 1 - 5: \n')
    res = True
    while res:
        game_level = input()
        if game_level.isnumeric():
            res = input_validation(int(game_level), 5)
        else:
            res = input_validation(game_level, 5)
    print(f'You choose game option number : {game_num} with game level number: {game_level} \n')
    if int(game_num) == 1:
        res = play_memory_game(int(game_level))
    elif int(game_num) == 2:
        res = play_guess_game(int(game_level))
    else:
        res = play_currency_roulette_game(int(game_level))
    if res:
        add_score(int(game_level))
    content_html = score_server()
    insert_text_to_file('index.html', content_html)
    app.run(debug=True, use_reloader=False)  # calling the flask application
