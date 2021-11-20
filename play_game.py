#!/usr/bin/env python3

# Author: Julianne Koenig
# Date Created: 8/2/19
# Last Modified: 11/20/2021
# Project: Hangman

from hangman import Hangman
import argparse

# Uses the Hangman class to create a running game of Hangman

def get_filename():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    return args.filename

def closing_message(num_games, num_won):
    print('\nThanks for playing!')
    print(f'Games played: {num_games}')
    print(f'Games won: {num_won}')
    pass

def play_game(filename=get_filename()):
    games_played = 0
    win_count = 0
    keep_playing = 'y'

    while keep_playing == 'y':
        game = Hangman()
        game.play(filename)
        games_played += 1
        if game.win == True:
            win_count += 1

        keep_playing = input('Keep playing? Enter \'y\' for yes and \'n\' for no: ')
        # make lowercase if not
        if keep_playing.islower() != True:
            keep_playing = keep_playing.lower()
        while keep_playing != 'y' and keep_playing != 'n':
            keep_playing = input('Invalid. Enter \'y\' for yes and \'n\' for no: ')
            if keep_playing.islower() != True:
                keep_playing = keep_playing.lower()

    closing_message(games_played, win_count)

if __name__ == '__main__':
    play_game()