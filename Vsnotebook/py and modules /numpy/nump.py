import numpy as np

print(np.__version__)


# array = np.array([1, 2, 3, 4, 5])
# print("Array:", array)
# print(type(array))

# arat = array * 2
# print("Array multiplied by 2:", arat)

# # THIS ARE THE EXAMPLES OF NDARRAY AND MULTIDIMENSIONAL ARRAYS

# # example of 0 dimensional array
# zero_d_array = np.array(42)
# print(zero_d_array.ndim)
# print("0D Array:", zero_d_array)


# # example of 1 dimensional array
# one_d_array = np.array([10, 20, 30, 40, 50])

# print(one_d_array.ndim)
# print("shape of the array is : ", one_d_array.shape)
# print("1D Array:", one_d_array)

# #example of 2 dimensional array
# two_d_array = np.array([[1, 2, 3],
#                         [4, 5, 6]]
#                         )

# print(two_d_array.ndim)
# print("shape of the array is : ", two_d_array.shape)
# print("2D Array:\n", two_d_array)

# # example of 3 dimensional array
# three_d_array = np.array([
#     [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
#     [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']],
#     [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]
# ])

# print(three_d_array.ndim)
# print("shape of the array is : ", three_d_array.shape)
# print("3D Array:\n", three_d_array)
# print(three_d_array[0][0][0]) #this is called chain indexing 



# word = three_d_array[0, 0, 0] + three_d_array[2,0, 0 ] + three_d_array[1,0,0] #string concatenation using chain indexing 

# print(word)


# SLICING USING NUMPY ARRAYS 

#Using 2D array

# array_2d = np.array([[10, 20, 30, 40, 50],
#                      [60, 70, 80, 90, 100],
#                      [110, 120, 130, 140, 150],
#                      [160, 170, 180, 190, 200]])

# print(array_2d[1 ,2]) 

# array[start:end:step]

# print(array_2d[0]) #First row 
# print(array_2d[1]) #Second row
# print(array_2d[2]) #Third row
# print(array_2d[3]) #Fourth row

# print(array_2d[:, 0]) #First column
# print(array_2d[:, 1]) #Second column
# print(array_2d[:, 2]) #Third column
# print(array_2d[:, 3]) #Fourth column


# print(array_2d[0:4:2]) #Slicing rows with step of 2

# print(array_2d[:,0:3]) #Slicing columns from index 0 to 2

# print(array_2d[:, ::-1]) #Reversing the columns

# print(array_2d[0:2, 0:2]) #Slicing a sub-array from the 2D array


'''RANDOM ARRAY GENERATION AND RESHAPING '''

array = np.arange(6) # Creating a 1D array with values from 0 to 5
print("Original array:", array)
print("Original shape:", array.shape)  # Output: (6,)

re_shap = array.reshape(3, 2) # Reshaping to 2D array with 3 rows and 2 columns
print("Reshaped array (3x2):\n", re_shap)


print("\n" + "="*50)
print("USING np.newaxis TO ADD A NEW DIMENSION")
print("="*50 + "\n")

# Method 1: Convert 1D array to COLUMN VECTOR (n, 1)
column_vector = array[:, np.newaxis]
print("Shape:", column_vector.shape)  # Output: (6, 1)
print(column_vector)

print("\n" + "-"*50 + "\n")

# Method 2: Convert 1D array to ROW VECTOR (1, n)
row_vector = array[np.newaxis, :]
print("Shape:", row_vector.shape)  # Output: (1, 6)
print(row_vector)

print("\n" + "-"*50 + "\n")

# You can also use None instead of np.newaxis (they are equivalent)
column_with_none = array[:, None]
print("Shape:", column_with_none.shape)  # Output: (6, 1)
print(column_with_none)

print("\n" + "="*50)
print("PRACTICAL EXAMPLE: Broadcasting with np.newaxis")
print("="*50 + "\n")

# Create two 1D arrays
a = np.array([1, 2, 3])
b = np.array([10, 20, 30, 40])

print("Array a:", a, "shape:", a.shape)
print("Array b:", b, "shape:", b.shape)

# To perform operations between arrays of different shapes, use np.newaxis
# Convert 'a' to column vector and 'b' stays as row (or make it explicit)
result = a[:, np.newaxis] + b[np.newaxis, :]
print("\nBroadcasting addition (a as column + b as row):")
print("Result shape:", result.shape)  # Output: (3, 4)
print(result)
# Each element of 'a' is added to each element of 'b'

