"""
CMSC 14200, Winter 2026
Homework 5

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import pandas as pd

# load data
athlete_data = pd.read_csv("data_olympics/athlete_events.csv")
NOC_name = pd.read_csv("data_olympics/noc_regions.csv")

def filter_data(starting_df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter the DataFrame such that it only contains the data necessary:

    1. Remove the superfluous columns from your DataFrame
    2. Filter only for rows that are from a winter olympic game
    3. Filter only for rows that won medals

    4. Remove any rows that would cause you to over-count the number
       of decorated athletes
    """
    raise NotImplementedError('filter_data')


def create_medal_data(filtered_df: pd.DataFrame) -> pd.DataFrame:
    """
    Produce a DataFrame where each row should represent the number
    of decorated athletes, from a certain country, in a certain year
    of the winter olympics with the columns Year, NOC, and
    Decorated_Athletes.
    """
    raise NotImplementedError('create_medal_data')


def create_ranking_dict(medal_data: pd.DataFrame) -> dict:
    """
    Create a dictionary to use in the bar chart. The format should be:

    {1924: [
      {'Decorated_Athletes': 31, 'Flag': 'united-kingdom.bmp', 'NOC': 'GBR'},
      {'Decorated_Athletes': 12, 'Flag': 'united-states.bmp', 'NOC': 'USA'},
      {'Decorated_Athletes': 10, 'Flag': 'france.bmp', 'NOC': 'FRA'},
      {'Decorated_Athletes': 9, 'Flag': 'canada.bmp', 'NOC': 'CAN'},
      {'Decorated_Athletes': 9, 'Flag': 'finland.bmp', 'NOC': 'FIN'}
    ]}
    """
    raise NotImplementedError('create_ranking_dict')
