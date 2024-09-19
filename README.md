# assignment3 NBA Player Statistics Analysis

This assignment involves analyzing player statistics from a CSV file using Python. The primary objectives are to load the data into NumPy arrays, perform data manipulation, and calculate various performance metrics for players

1. Class Design and Implementation
  Class: PlayerStatsAnalyzer
     This class is responsible for loading the data, cleaning it, calculating metrics, and identifying the top 100 players based on various performance metrics. 
 
2. Attributes
  df
  data
  player_col
  season_col
  fgm_col
  fga_col
  three_pm_col
  three_pa_col
  ftm_col
  fta_col
  pts_col
  min_col
  blk_col
  gp_col
  stl_col

3. Methods

__init__(self, csv_file): Initializes the class by loading the CSV file and cleaning the data.
calculate_metrics(self): Calculates various performance metrics.
get_top_100_players(self, metric_index): Returns the top 100 players for a given metric.
print_results(self): Prints the top 100 players for each metric.


Conclusion:
 
  This assignment demonstrates how to load, clean, and manipulate data using pandas and NumPy.
