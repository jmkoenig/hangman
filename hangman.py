# Author: Julianne Koenig
# Date: 8/2/19
# Project: Hangman

import os
from random import randint

class Hangman:
    def __init__(self):
        self.gameboard = ['?', '?', '?', '?', '?']
        self.game_word = None
#        self.man = ('O', '|', '\\', '/', '\\', '/')
        self.limb_count = 0
        self.guess_list = []
        self.win = False

    # print gameboard
    def print_board(self):
        for letter in self.gameboard:
            print(letter, end='')
        print('\n')

    # print hangman
    def print_man(self):
        if self.limb_count == 0:
            stand = [' ____', '\n |', '  |', '\n |', '\n |', '\n |', '\n |', '\n---']
        elif self.limb_count == 1:
            stand = [' ____', '\n |', '  |', '\n |', '  O', '\n |', '\n |', '\n |', '\n---']
        elif self.limb_count == 2:
            stand = [' ____', '\n |', '  |', '\n |', '  O', '\n |', '  |', '\n |', '\n |', '\n---']
        elif self.limb_count == 3:
            stand = [' ____', '\n |', '  |', '\n |', '  O', '\n |', ' \\', '|', '\n |', '\n |', '\n---']
        elif self.limb_count == 4:
            stand = [' ____', '\n |', '  |', '\n |', '  O', '\n |', ' \\', '|', '/', '\n |', '\n |', '\n---']
        elif self.limb_count == 5:
            stand = [' ____', '\n |', '  |', '\n |', '  O', '\n |', ' \\', '|', '/', '\n |', ' /', '\n |', '\n---']
        else:
            stand = [' ____', '\n |', '  |', '\n |', '  O', '\n |', ' \\', '|', '/', '\n |', ' /', ' \\', '\n |', '\n---']
        
        for part in stand:
            print(part, end='')
        print('\n')


    # eventually have words of different length;
    # will need a function that gets the length of game word
    # and makes game board of that length

    # use a random number to pick a word from the text file
    def choose_word(self, filename):
        with open(filename) as words_file:
           lines = words_file.readlines()
           rand_num = randint(0, len(lines)-1)
           # strip the newline character from the word
           self.game_word = lines[rand_num].rstrip('\n')

    # compare guessed letter to each letter in the word
    def check_letter(self, guess):
        in_word = False
        index = -1
        if guess not in self.guess_list:
            # add guess to guess list
            self.guess_list.append(guess)
            for letter in self.game_word:
                index += 1
                # if guess is same as letter in word, add it to the gameboard
                if guess == letter:
                    in_word = True
                    self.gameboard[index] = guess

            # add to limb count if guess isn't in word
            if not in_word:
                self.limb_count += 1
        else:
            new_guess = input('Letter was already guessed. Guess again: ')
            self.check_letter(new_guess)

    # check that guessed word is the same as game word
    def guess_word(self):
        guess = input('Guess word: ')
        # if they're not the same, make limb count 6 so it signals a loss
        if guess != self.game_word:
            self.limb_count = 6
        # else make the gameboard match the word so there's no more ?'s
        else:
            index = 0
            for letter in self.game_word:
                self.gameboard[index] = letter
                index += 1

    def play(self, filename):
        print('\nWelcome to Hangman! Enter a letter, or enter \'guess\' to guess the word.'
            '\nIf your guessed word is incorrect, you lose the game.')
        self.choose_word(filename)
        guess = ''
        # loop only if gameboard isn't filled and man isn't completely drawn
        while '?' in self.gameboard and self.limb_count < 6:
            self.print_man()
            self.print_board()
            guess = input('Guess a letter, or enter \'guess\' to guess the word: ')
            if guess == 'guess':
                self.guess_word() 
                break
            while len(guess) != 1:
                guess = input('Invalid guess. Guess again: ')
            self.check_letter(guess)
    
        if self.limb_count == 6:
            self.print_man()
            print('You lost!')
        else:
            print('\nYou won!')
            self.win = True
        print(f'\nThe word was {self.game_word}\n')
        
