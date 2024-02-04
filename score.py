from os import path
from pathlib import Path
from utils import scores_file_name


def add_score(difficulty):
    point_of_winning = difficulty * 3 + 5
    print(f'You won: {point_of_winning} points in your last game..  \n')
    if not path.exists(scores_file_name):  # first game, checking if the file is exist or not
        file = open(scores_file_name, 'w')
        final_point_of_winning = point_of_winning
        print('Since this is your first game..')
    else:
        file = open(scores_file_name, 'r+')
        current_points = file.read()
        final_point_of_winning = point_of_winning + int(current_points)
        file.seek(0)  # move the file cursor to beginning
    file.write(str(final_point_of_winning))
    print(f'Your final total score till now is  : {final_point_of_winning}, Well Done -:) \n')
    file.close()



