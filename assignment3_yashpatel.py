import pandas as pd
import numpy as np

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('players_stats_by_season_full_details.csv')

# Calculate metrics
df['FG_accuracy'] = df['FGM'] / df['FGA']
df['3P_accuracy'] = df['3PM'] / df['3PA']
df['FT_accuracy'] = df['FTM'] / df['FTA']
df['PTS_per_min'] = df['PTS'] / df['MIN']
df['overall_accuracy'] = (df['FGM'] + df['3PM'] + df['FTM']) / (df['FGA'] + df['3PA'] + df['FTA'])
df['BLK_per_game'] = df['BLK'] / df['GP']
df['STL_per_game'] = df['STL'] / df['GP']

# Rank players and select the top 100 for each metric
metrics = ['FG_accuracy', '3P_accuracy', 'FT_accuracy', 'PTS_per_min', 'overall_accuracy', 'BLK_per_game', 'STL_per_game']
top_100_players = {}

for metric in metrics:
    top_100_players[metric] = df.nlargest(100, metric)[['Player', 'Season', metric]]

# Convert the DataFrame to Numpy ndarrays
top_100_ndarrays = {metric: top_100_players[metric].to_numpy() for metric in metrics}

# Accessing the top 100 players for field goal accuracy
top_100_fg_accuracy = top_100_ndarrays['FG_accuracy']
print(top_100_fg_accuracy)

# Create a list of the top 100 players and corresponding season for each metric
top_100_list = {metric: top_100_players[metric].values.tolist() for metric in metrics}

#Accessing the list of top 100 players for field goal accuracy
top_100_fg_accuracy_list = top_100_list['FG_accuracy']
print(top_100_fg_accuracy_list)

#accessing the list of top 100 players for 3pt accuracy
top_100_3pt_accuracy_list = top_100_list['3P_accuracy']
print(top_100_3pt_accuracy_list)

#accessing the list of top 100 players for free throw accuracy
top_100_fg_accuracy_list = top_100_list['FT_accuracy']
print(top_100_fg_accuracy_list)

#accessing the list of top 100 players for points per minute
top_100_pts_per_min_list = top_100_list['PTS_per_min']
print(top_100_pts_per_min_list)

#accessing the list of top 100 players for overall accuracy
top_100_overall_accuracy_list = top_100_list['overall_accuracy']
print(top_100_overall_accuracy_list)

#accesing the list of top 100 players for blocks per game
top_100_blk_per_game_list = top_100_list['BLK_per_game']
print(top_100_blk_per_game_list)

top_100_steals_per_game_list = top_100_list['STL_per_game']
print(top_100_steals_per_game_list)