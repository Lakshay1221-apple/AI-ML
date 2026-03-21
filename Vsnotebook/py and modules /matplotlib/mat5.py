''' 
IN this file we are going to learn how to create histogram using matplotlib
Histogram = A graphical representation that organizes a group of data points into user-specified ranges.
It is used to visualize the distribution of a dataset and to identify patterns such as skewness, modality, and the presence of outliers.
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np      
mpl.use("TkAgg")

scores = np.random.normal(loc = 80, scale = 10, size = 100) # generate random scores following normal distribution   

plt.hist(scores,
         bins=10,  # number of bins
         color='skyblue',
         edgecolor='black',
         alpha=0.7)  # transparency     

plt.title("Distribution of Scores", fontsize=20, fontweight='bold', color='darkblue')
plt.xlabel("Scores", fontsize=14, color='green')
plt.ylabel("Frequency", fontsize=14, color='green')

plt.show()  # display the plot