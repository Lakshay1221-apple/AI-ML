# THIS IS THE FIRST FOLDER FOR PANDAS MODULES, it is used in Data Analysis and Data Science Projects, Pandas = panel data 

'''
Pandas works with dat frames which are of two types:
1. Series - 1D labeled array capable of holding any data type, like a single column of a spreadsheet 
2. DataFrame - 2D labeled data structure with columns of potentially different types

'''


from calendar import Day
import pandas as pd 


# print(pd.__version__)
# IN THIS FILE WE WILL LEARN ABOUT PANDAS SERIES

# USING LIST FOR SERIES CREATION

data = [100, 102, 104, 200, 202]


# series = pd.Series(data, index = ["appartment #1", "appartment #2", "appartment #3", "appartment #4", "appartment #5"])  # Creating a Pandas Series from a list
# print(series)


# print(series.loc['appartment #2'])  # Accessing data using label-based indexing
# print(series.iloc[2])  # Accessing data using integer-based indexing

# series.loc['appartment #3'] = 110  # Modifying data in the Series
# print(series)

# print(series[series >= 200])  # Filtering data in the Series based on a condition


# USING DICTIONARY FOR SERIES CREATION

calories = {'day 1': 1750, 'day 2': 2100, 'day 3': 1700}

series = pd.Series(calories)  # Creating a Pandas Series from a dictionary
# print(series)

# print(series['day 2'])  # Accessing data using label-based indexing

series['day 3'] += 500  # Modifying data in the Series
# print(series)

print("on this day i had less than 2000 calories : ", series[series < 2000])  # Filtering data in the Series based on a condition