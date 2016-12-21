#! /usr/bin/env python3

""" Imports """

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
csv_file_01 = open('/Users/SMcGhin/Documents/python/data_sets/game-of-thrones/battles.csv', 'rt')
data = pd.DataFrame(pd.read_csv(csv_file_01))
# print(data.head())


# Get basic quartile info about our dataset
# print(data.describe())


# Total Battles by House
# house_battles = data[['attacker_1', 'attacker_outcome']].groupby(['attacker_1']).count()
# house_battles.columns = ['total_battles']
# house_battles.sort_values(by='total_battles', ascending=False)\
#     .plot(kind='bar', color=['#FC4F30'], grid=False, legend=None, fontsize=10, title='Battles Fought by House')
# mp.show()
# print(house_battles)
# Battles Won by House
# wins = data[['attacker_1', 'attacker_outcome']]
# house_wins = wins[wins['attacker_outcome'] == 'win'].groupby(['attacker_1']).count()
# house_wins.columns = ['battles_won']
# print(house_wins)
# win_percent = (house_wins.battles_won/house_battles.total_battles) * 100
# win_percent.columns = ['% Battles Won']
# wins_table = house_wins.join(house_battles)
# wins_table.sort_values(by='total_battles', ascending=False)\
#     .plot(kind='bar', fontsize=10, grid=False, title='Battles Won to Fought')
# mp.show()


# Won Battles Over Time
# time_battles = data[['year', 'name', 'attacker_1', 'attacker_size']].fillna(0)
# time_set_filter = time_battles[time_battles['attacker_1'] == 'Lannister']
# troops = time_set_filter.groupby(['year', 'name']).sum()
# battles_table = time_battles.groupby(['year', 'attacker_1', 'name']).sum()
# print(battles_table)
# troops.unstack().plot(kind='bar', stacked=True, title='Lannister Troops by Battle')
# mp.show()


"""

Character Deaths Data Set

"""

# Create character death data frame object with which to work
# csv_file_02 = open('/Users/SMcGhin/Documents/python/data_sets/game-of-thrones/character-deaths.csv', 'rt')
# death_data = pd.DataFrame(pd.read_csv(csv_file_02))
# death_data['Allegiances'] = death_data['Allegiances'].str.replace('House ', '')  # Remove House prefix to group values
# print(death_data.head())

# Count character deaths by allegiance
# fil_char_deaths_01 = death_data[death_data['Allegiances'] != 'None']  # Filter out unwanted alignments
# fil_char_deaths_02 = fil_char_deaths_01[fil_char_deaths_01['Allegiances'] != 'Wildling']
# fil_char_deaths_03 = fil_char_deaths_02[fil_char_deaths_02['Allegiances'] != "Night's Watch"]
# char_deaths = fil_char_deaths_03[['Name', 'Allegiances']].groupby(['Allegiances']).count()
# char_deaths.columns = ['total_deaths']
# print(char_deaths)

# Basic bar showing deaths by house
# char_deaths.sort_values(by='total_deaths')\
#     .plot(kind='barh', color=['#FC4F30'], grid=False, legend=None, title='Character Deaths by House Alignment')
# mp.show()

# Plot number of noble deaths per total deaths by house
# noble_deaths_filter = fil_char_deaths_03[fil_char_deaths_03['Nobility'] == 1]  # Build noble death column
# noble_table = noble_deaths_filter[['Name', 'Allegiances']].groupby(['Allegiances']).count()
# noble_table.columns = ['noble_deaths']
# noble_death_table = noble_table.join(char_deaths)  # Join to existing table to plot
# print(noble_death_table)
# noble_death_table.sort_values(by='total_deaths', ascending=False)\
#     .plot(kind='bar', grid=False, title='House Noble Deaths to Total')
# mp.show()

# Get % of Deaths to Total Deaths
# death_perc = (char_deaths/char_deaths.sum()) * 100
# death_perc.columns = ['perc_tot_deaths']
# print(death_perc)

# Donut Chart for % of Death Total
# death_perc.plot(kind='pie', subplots=True, legend=False, title='Proportion of All Named Deaths')
# center_circle = mp.Circle((0, 0), 0.75, color='black', fc='white', linewidth=1.25)  # Draw circle in center
# fig = mp.gcf()
# fig.gca().add_artist(center_circle)
# mp.axis('equal')  # Set aspect ratio to be equal so drawn as circle
# mp.show()



