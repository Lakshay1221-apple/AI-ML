# IN THIS FILE WE WILL LEARN ABOUT BROADCASTING IN NUMPY 

'''Braodcasting allows Numpy to perform operations on arrays of different shapes by virtually expanding dimensions so they match the large array shape '''
""" the dimensions have the same size or one of the dimensions have the size of 1"""

import numpy as np

# array1 = np.array([[1, 2, 3, 4]])

# array = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8]])

# array2 = np.array([[10],
#                    [20],
#                    [30],
#                    [40]])

# print(array1.shape)  # Output: (1, 4) 1 row and 4 columns
# print(array.shape)   # Output: (2, 4) 2 rows and 4 columns
# print(array2.shape)  # Output: (4, 1) 4 rows and 1 column

# print(array + array1)  # Broadcasting array1 to match array's shape
# print(array1 + array2)  # Broadcasting array2 to match array's shape
# # print(array2 * array) #error because shapes are not compatible for broadcasting


''' Creating multiplication table using broadcasting '''

array1 = np.array([[1, 2 ,3 ,4, 5, 6, 7, 8, 9 , 10]])
array2 = np.array([[1],
                   [2],
                   [3],
                   [4],
                   [5],
                   [6],
                   [7],
                   [8],
                   [9],
                   [10]])

print(array1.shape) # Output: (1, 10) this means 1 row and 10 columns
print(array2.shape) # Output: (10, 1) this means 10 rows and 1 column

multiplication_table = array2 * array1  # Broadcasting to create multiplication table
print(multiplication_table) # 10x10 multiplication table

print('This is called numpy broadcasting')






