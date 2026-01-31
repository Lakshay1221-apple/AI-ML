'''
In this file we will learn how to do Data cleaning using Pandas module
Data cleaning = process of identifying and correcting (or removing) errors and inconsistencies from data to ensure the quality and accuracy of the dataset.
`75% of work done with pandas in data cleaning 
'''

import pandas as pd 
df = pd.read_csv('data/poki.csv')

# Drop irrelevant columns 
# df.drop(columns=["Legendary"], inplace = True) #drops the column permanently
# print(df.head())

# Handle missing values 

# df = df.dropna(subset = ["Type2"]) #drops rows with NaN in Type2 column
# print(df.head())


#How to fill missing values
# df = df.fillna({"Type2": "Unknown"}) #fills NaN in Type2 column with 'Unknown'
# print(df.head())


#HOW TO fix inconsistent DATA

# df["Type1"] = df["Type1"].replace({"Grass": "Tree", 
#                                    "Fire" : "Flame",
#                                    "Water" : "Aqua"}) #replaces values in Type1 column
# print(df.head(10))

# How ro standardize text data

# df["Name"] = df['Name'].str.lower() #converts all names to lowercase
# print(df.head(10))


# HOW TO FIX OR CHANGE DATA TYPES

# df["Legendary"] = df["Legendary"].astype(bool) #converts Legendary column to integer type
# print(df.tail(10))

# REMOVE DULPICATES VALUES 

df = df.drop_duplicates() #removes duplicate rows
print(df)