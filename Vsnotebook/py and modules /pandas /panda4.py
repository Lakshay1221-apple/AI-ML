'''
IN THIS FILE WE WILL LEARN HOW TO DO FILTERING IN DATA FRAME USING PANDAS MODULE
'''
import pandas as pd 

df = pd.read_csv('data/poki.csv')

# tall_pokemon = df[df['Height'] > 2]  # FILTERING POKEMON WITH HEIGHT GREATER THAN 2
# print("Tall Pokemon (Height > 2):")
# print(tall_pokemon)

# fire_type_pokemon = df[df['Type1'] == 'Fire']  # FILTERING POKEMON OF TYPE 'Fire'
# print("\nFire Type Pokemon:")
# print(fire_type_pokemon)

# legandary = df[df['Legendary'] == True]  # FILTERING LEGENDARY POKEMON
# print("\nLegendary Pokemon:")
# print(legandary)

# water_pokemon = df[(df['Type1'] == "Water") |
#                    (df['Type2'] == "Water")]  # FILTERING POKEMON OF TYPE 'Water'
# print("\nWater Type Pokemon:")
# print(water_pokemon)

ff_pokemon = df[(df['Type1'] == "Fire") & # FILTERING POKEMON WITH EITHER TYPE1 OR TYPE2 AS 'Fire' and 'Flying'
                (df["Type2"] == "Flying")]
print("\nFire Type Pokemon:")
print(ff_pokemon)


