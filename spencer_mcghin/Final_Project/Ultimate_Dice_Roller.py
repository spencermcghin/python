#! /usr/bin/env python

"""

DICE ROLLER FOR ALL YOUR GAMING NEEDS!
This program will allow a user to pick from a number of dice types
and roll them individually, in multiples of the same dice, or as an assortment
of different dice.

"""

# Imports
import random


# Define Global Variables
""" Dict object that takes user input (keys) and matches it with the side (value). """

side_dict = {"1": [2],
             "2": [4],
             "3": [6],
             "4": [8],
             "5": [10],
             "6": [12],
             "7": [20],
             "8": [100]}

""" List objects that are used to generate menu in dice_menu. """

dice_list = ["d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100"]

number_of_dice = [str(x) + '.' for x in range(1, len(dice_list) + 1)]


# Classes
class Dice(object):
    selection_list = []

    def __init__(self, side, number):
        self.side = side
        self.number = number

    @staticmethod
    def add_dice(side, number):
        """ Add selected number of dice to selection list object. """
        Dice.selection_list.extend(number * side)

    def get_dice_value(self):
        """ Returns random value for each die selected
         and then updates it to the die_roll_dict object for printing later. """
        die_roll_dict = {}
        for die in self.selection_list:
            if die in side_dict:
                die_roll_dict[die] = [random.randint(1, self.side)]


# Functions for main program
def main():
    print("Hail champion and welcome to the Super Dice Roller!" '\n'
          "Please choose a dice to roll from the menu below, and then follow any additional instructions." '\n'
          "You'll be able to choose more and/or different dice afterwards.")
    dice_menu()


def dice_menu():
    """ Print out menu of dice options. """
    dice_options = zip(number_of_dice, dice_list)
    for number, dice in dice_options:
        print(number, dice)
    while True:
        user_input = input("> ") + '.'
        if user_input not in number_of_dice:
            print("Please try again.")
        else:
            die_amount_selector(user_input)


def die_amount_selector(user_input):
    """ Prompt user for amount of dice to roll and then add to selection_list object. """
    try:
        die_amount = int(input("How many would you like to roll? '\n> "))
    except ValueError:
        print("Please enter an appropriate value.")
        die_amount_selector(user_input)
    else:
        Dice.add_dice(side=user_input.strip('.'), number=die_amount)
        print(Dice.selection_list)
        roll_more_prompt()


def roll_more_prompt():
    """ Check with user if they would like to roll more / different dice. """
    print("Would you like to roll any additional dice?")
    while True:
        confirm = input("Yes (y) or No (n)? '\n> ")
        if confirm == 'y':
            dice_menu()
        elif confirm == 'n':
            Dice.get_dice_value()


if __name__ == '__main__':
    main()
