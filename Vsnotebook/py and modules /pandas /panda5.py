'''
In this file we will learn about aggregate function
aggregate function = Reduce a set of values into a single summary value used to summarize and analyze data often used with the groupby() function

it uses following functions:
1. sum() - calculates the sum of values
2. mean() - calculates the average of values
3. median() - calculates the median of values           
4. min() - finds the minimum value
5. max() - finds the maximum value
6. count() - counts the number of non-null values
7. std() - calculates the standard deviation
8. var() - calculates the variance

note: These functions can be applied to DataFrames and Series objects in pandas to perform data analysis and summarization(0nly numeric).
'''


import pandas as pd

df = pd.read_csv('data/poki.csv')

# FOR THE COMPLETE DATAFRAME

# print("\nMean Value:")
# print(df.mean(numeric_only=True))  # Calculate the mean of numeric columns

# print("\nSum Value:")
# print(df.sum(numeric_only=True))   # Calculate the sum of numeric columns

# print("\nMin Value:")
# print(df.min(numeric_only=True))   # Find the minimum value in numeric columns

# print("\nMax Value:")
# print(df.max(numeric_only=True))   # Find the maximum value in numeric columns

# print("\nCount Value:")
# print(df.count())                  # Count the number of non-null values in each column

# print("\nStandard Deviation Value:")
# print(df.std(numeric_only=True))   # Calculate the standard deviation of numeric columns

# print("\nVariance Value:")  
# print(df.var(numeric_only=True))   # Calculate the variance of numeric columns

# print("\nMedian Value:")
# print(df.median(numeric_only=True))# Calculate the median of numeric columns


# FOR SINGLE COLUMN

# print("\nMean Height Value:")
# print(df['Height'].mean(numeric_only=True))  # Calculate the mean of height columns

# print("\nSum Height Value:")
# print(df['Height'].sum(numeric_only=True))  # Calculate the sum of height columns

# print("\nMin Height Value:")
# print(df['Height'].min(numeric_only=True))  # Find the minimum value in height columns



# GEOUPBY() FUNCTION
'''
df.groupby('Type1')
This groups all rows that share the same value in Type1.
For example, all Fire Pokémon together, all Water together, all Dragon together, etc.

['Height']
From each group, it selects only the Height column.

.mean()
It computes the average (mean) height within each group.
'''
print("\nMean Height by Type 1:")
print(df.groupby('Type1')['Height'].mean())  # Group by 'Type 1' and calculate the mean of 'Height' for each group

print("\nSum Height by Type 1:")
print(df.groupby('Type1')['Height'].sum())  # Group by 'Type 1' and calculate the sum of 'Height' for each group




