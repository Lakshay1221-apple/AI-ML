# IN THIS FILE WE WILL LEARN ABOUT FILTERING USING NUMPY 
''' Filtering refres to the process of selecting elements from an array that match a given condition'''

import numpy as np

ages = np.array([[22, 25, 18, 30, 27, 19, 65, 21],
                [12, 15, 28, 20, 17, 16, 26, 23]])


teenagers = ages[(ages >= 13) & (ages <= 19)]  # Filtering ages between 13 and 19
print("Teenagers ages are:", teenagers)

adults = ages[ages >= 20]  # Filtering ages 20 and above
print("Adults ages are:", adults)

seniors = ages[ages >= 60]  # Filtering ages 60 and above
print("Senior citizens ages are:", seniors)

even_ages = ages[ages % 2 == 0]  # Filtering even ages
print("Even ages are:", even_ages)

odd_ages = ages[ages % 2 != 0]  # Filtering odd ages
print("Odd ages are:", odd_ages)    


'''
np.where(condition, value_if_true, value_if_false)

'''

adultss = np.where(ages >= 18, ages, 0)  # Using np.where to filter adults, replacing others with 0
print("Ages with adults and 0 for others:", adultss)