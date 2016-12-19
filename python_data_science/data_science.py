#! /usr/bin/env python3

""" Imports """

import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
mp.style.use('fivethirtyeight')


""" Config changes """

# Enable pycharm interactive mode for display of charts
mp.interactive(False)

# Configure data frame display output
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)


""" Functions """

# Create data frame object with which to work
csv_file = open('/Users/SMcGhin/Documents/python/data_sets/vgsales.csv', 'rt')
data = pd.DataFrame(pd.read_csv(csv_file, parse_dates=['Year']))


# Get basic quartile info about our dataset
print(data.describe())


# Matplotlib figure - Yearly Sales
# na_sales = data[['Year', 'NA_Sales']]
# year_group = na_sales.groupby('Year')
# na_sales_totals = year_group.sum()
# na_sales_totals.plot(kind='line', legend=None, title='Yearly North American Sales')
# mp.show()

# Matplotlib figure - Sales by Category
# genre_sales = data[['Year', 'Genre', 'Global_Sales']]
# genre_group = genre_sales.groupby(['Year', 'Genre']).sum()
# genre_group.unstack().plot(kind='bar', stacked=True, title='Yearly Global Sales by Genre')
# mp.show()

