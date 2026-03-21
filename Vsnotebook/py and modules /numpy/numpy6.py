# IN THIS FILE WE WILL HOW TO GENERATE AND OPERATE ON RANDOM NUMBERS USING NUMPY

import numpy as np

rng = np.random.default_rng()
print("Random integers between 0 and 10:", rng.integers(0, 11, size=5))  # Generate 5 random integers between 0 and 10


# FLOATING POINT NUMBERS

print(np.random.uniform(0.0, 1.0, size=5))  # Generate 5 random floats between 0.0 and 1.0

