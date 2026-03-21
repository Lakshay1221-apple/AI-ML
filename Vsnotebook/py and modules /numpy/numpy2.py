# IN THIS FILE, WE WILL LEARN ABOUT SCALAR ARITHMETICS, VECTORIZED MATH FUNCTIONS,

import numpy as np

#SCALAR ARTHMETICS

# array = np.array([1, 2, 3, 4, 5])

# print(array + 1) #adding 1 to each element
# print(array - 1) #subtracting 1 from each element
# print(array * 2) #multiplying each element by 2
# print(array / 2) #dividing each element by 2
# print(array ** 2) #squaring each element
# print(array % 2) #modulus of each element by 2

# Vactorized math functions 

# arra = np.array([1, 2, 3])

# print(np.sqrt(arra)) #square root of each element
# print(np.floor(arra)) #floor of each element
# print(np.round(arra)) #rounding of each element
# print(np.ceil(arra)) #ceiling of each element
# print(np.exp(arra)) #exponential of each element
# print(np.log(arra)) #natural logarithm of each element
# print(np.sin(arra)) #sine of each element
# print(np.cos(arra)) #cosine of each element
# print(np.tan(arra)) #tangent of each element



# Q - Radius given, convert it to the area  and circumference of circle 
# radius = np.array([1, 2, 3, 4, 5])

# area = np.pi * np.square(radius)
# circumference = 2 * np.pi * radius

# print("The circumference of the circle is:", circumference)
# print("Area of circles with given radius:", area)


# ELEMETNT WISE ARITHMETICS 

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])

# print(array1 + array2) # element wise addition
# print(array1 - array2) # element wise subtraction
# print(array1 * array2) # element wise multiplication
# print(array1 / array2) # element wise division
# print(array1 ** array2) # element wise exponentiation
# print(array1 % array2) # element wise modulus


# COMPARION OPERATORS

scores = np.array([85, 90, 100, 92, 88, 55])

print(scores == 100)  # Check for equality with 100 and return boolean array
print(scores > 90)    # Check for scores greater than 90
print(scores < 90)    # Check for scores less than 90
print(scores >= 88)   # Check for scores greater than or equal to 88    
print(scores < 60)  # Check for scores less than 60

scores[scores < 60] = 0  # Set scores less than 60 to 0
print("Updated Scores:", scores)