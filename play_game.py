#!/usr/bin/env python

# Author: Julianne Koenig
# Date: 8/2/19
# Project: Hangman

from hangman import Hangman
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

games_played = 0
win_count = 0
keep_playing = 'y'
while keep_playing == 'y':
    game = Hangman()
    game.play(args.filename)
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

print('\nThanks for playing!')
print(f'Games played: {games_played}')
print(f'Games won: {win_count}')
