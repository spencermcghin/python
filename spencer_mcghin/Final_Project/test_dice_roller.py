#!/usr/bin/env python

""" Test code for Ultimate_Dice_Roller.py """

from Ultimate_Dice_Roller import Dice


def test_roll_dice():
    d = Dice()
    d.roll_dice('3', 5)
    for k in d.roll_dict.keys():
        print(k)
        assert k == 'd6'
    for k, v in d.roll_dict.items():
        print(v)
        assert len(v) == 5

def test_die_amount_selector():
