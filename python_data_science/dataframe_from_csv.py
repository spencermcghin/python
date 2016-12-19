#! /usr/bin/env python3


""" Imports """
import pandas as pd


def build_dataframe(file):
    with open(file, 'rt') as csv_file:
        data = pd.DataFrame(pd.read_csv(csv_file))
        return data


build_dataframe('/Users/SMcGhin/Documents/python/data_sets/vgsales.csv')