#! /usr/bin/env python3

""" Imports """

import sys
import pandas as pd


""" Read in csv. Must pass file argument. """


def read_csv(file):
    with open(file, 'rt') as csv_file:
        games_data = pd.read_csv(csv_file)
        return games_data
