''' 
In this file we will learn how to create scatter plots using matplotlib
scatter grahs = Shows the relationship between two different variables, helps to identify a correlation (+, - , none)
ex = study hour vs marks obtained 
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.use("TkAgg")

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # study hours
y = np.array([10, 20, 25, 30, 40, 50, 55, 60, 70, 80]) # marks obtained

x2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # study hours
y2 = np.array([80, 70, 60, 55, 50, 40, 30, 25, 20, 10]) # marks obtained

style = {
    "scatter": dict(
        marker='o',
        s=100,  # size of markers
        c='purple',  # color of markers
        edgecolor='black',  # edge color of markers
        alpha=0.7,  # transparency
        label = "Positive Correlation"
    ),

    "scatter2": dict(
        marker='^',
        s=100,  # size of markers
        c='orange',  # color of markers
        edgecolor='black',  # edge color of markers
        alpha=0.7,  # transparency
        label = "Negative Correlation"
    )

}

plt.scatter(x, y, **style["scatter"])
plt.scatter(x2, y2, **style["scatter2"])

plt.title("Study Hours vs Marks Obtained", 
          fontsize = 20, 
          family = 'Arial', 
          fontweight = 'bold', 
          color = 'red') # title of the plot   

plt.xlabel("Study Hours", fontsize=14, color='green') # x-axis label
plt.ylabel("Marks Obtained", fontsize=14, color='green') # y-axis label

plt.xticks(fontsize=12, rotation=45, color='blue') # x-axis ticks
plt.yticks(fontsize=12, color='blue') # y-axis ticks

plt.legend()  # display legend (must be before show)
plt.show()  # display the plot