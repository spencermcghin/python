#! /usr/bin/env python3

""" Imports """

import pandas as pd

""" Functions """

# Configure data frame display output
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)


# Create data frame object with which to work
csv_file = open('/Users/SMcGhin/Documents/python/data_sets/vgsales.csv', 'rt')
data = pd.DataFrame(pd.read_csv(csv_file))


# Takes dim and fact column from data frame as input and outputs two columns
# grouping by the dim, and sums the fact
def sum_by_group(d, f):
    group = data.groupby(d)[f].sum()
    print(group)


# Displays statistical, quartile information given two dims as inputs
def describe_data_frame(dim1, dim2):
    print(data.groupby(dim1)[dim2].describe().unstack())


