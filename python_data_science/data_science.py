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
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1000)


""" Functions """

# Create data frame object with which to work
csv_file = open('/Users/SMcGhin/Documents/python/data_sets/game-of-thrones/battles.csv', 'rt')
data = pd.DataFrame(pd.read_csv(csv_file))
# print(data.head())


# Get basic quartile info about our dataset
# print(data.describe())


# % Battles Won by House
house_battles = data[['attacker_1', 'attacker_outcome']]
total_battles = pd.DataFrame(house_battles.groupby(['attacker_1']).count())
total_battles.columns = ['total_battles']
print(total_battles)
wins = house_battles[house_battles['attacker_outcome'] == 'win']
house_wins = pd.DataFrame(wins.groupby(['attacker_1']).count())
house_wins.columns = ['battles_won']
win_percent = pd.DataFrame((house_wins.battles_won/total_battles.total_battles) * 100)
win_percent.columns = ['% Battles Won']
wins_table = house_wins.join(total_battles)
wins_table.plot(kind='bar')
mp.show()




# Won Battles Over Time
# time_battles = data[['year', 'name', 'attacker_1', 'attacker_size']].fillna(0)
# time_set_filter = time_battles[time_battles['attacker_1'] == 'Lannister']
# troops = time_set_filter.groupby(['year', 'name']).sum()
# print(time_battles.groupby(['year', 'attacker_1', 'name']).sum())
# troops.unstack().plot(kind='bar', stacked=True, title='Lannister Troops by Battle')
# mp.show()





