# IN THIS FILE WE WILL LEARN HOW TO IMPORT AND WORK ON CSV FILES USING PANDAS MODULE 
import pandas as pd

# Import the JSON file
# df_json = pd.read_json('data/pokemon150.json')
# print("\n\nPoki Data from JSON:")
# print(df_json.head())  # Display the first few rows from JSON


# Import the poki data file
# df = pd.read_csv('data/poki.csv')
# print("\nPoki Data:")

# print(df.head())  # Display the first few rows 
# print(df) # Display the entire DataFrame

# print(df.to_string())  # Display the entire DataFrame as a string

#SELECTION BY COLUMNS

# print(df[['Name', "Height", 'Weight']]) # Accessing columns by labels

#SELECTION BY ROWS
df = pd.read_csv('data/poki.csv', index_col='Name')  # Set 'Name' column as index

# print(df.iloc[0:5])  # Accessing rows by integer location
# print(df.loc['Bulbasaur':'Charizard'])  # Accessing rows by label
# print(df.loc['Pikachu'])  # Accessing a single row by label

# CHECKNIG IF THE NAME EXIST IN THE DATAFRAME

P = input("Enter the name of the pokemon to check if it exists in the DataFrame: ")
try:
  
    pokemon_data = df.loc[P]
    print(f"\nData for {P}:")
    print(pokemon_data)

except KeyError:
    print(f"\n{P} does not exist in the DataFrame.")




