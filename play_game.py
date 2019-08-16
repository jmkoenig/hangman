#!/usr/bin/env python

# Author: Julianne Koenig
# Date: 8/2/19
# Project: Hangman

from hangman import Hangman
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

win_count = 0
keep_playing = 'y'
while keep_playing == 'y':
    game = Hangman()
    game.play(args.filename)
    if game.win == True:
        win_count += 1

    keep_playing = input('Keep playing? Enter \'y\' for yes and \'n\' for no: ')
    while keep_playing != 'y' and keep_playing != 'n':
        keep_playing = input('Invalid. Enter \'y\' for yes and \'n\' for no: ')

print('\nThanks for playing!')
print(f'Games won: {win_count}')
