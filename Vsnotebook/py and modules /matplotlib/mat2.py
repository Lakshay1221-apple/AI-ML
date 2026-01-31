'''
In this file we are going to learn how to create bar charts using matplotlib 
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.use("TkAgg")

categories = np.array(["Grains", "Fruits", "Vegetables", "Dairy", "Meat", "Sweets"])

values = np.array([30, 25, 15, 10, 15, 5])

styles = {
    "bars": dict(
        color="purple",
        edgecolor="black",
        linewidth=1,
        hatch="/"
    )
}

plt.bar(categories, values, **styles["bars"])   # FOR VERTICAL BARS
# plt.barh(categories, values, **styles["bars"]) # FOR HORIZONTAL BARS



plt.title("Bar Chart Example", 
          fontsize = 20, 
          family = 'Arial', 
          fontweight = 'bold', 
          color = 'darkblue') # title of the plot

plt.xlabel("Food Categories", fontsize=14, color='green') # x-axis label
plt.ylabel("Quantity", fontsize=14, color='green') # y-axis label

plt.xticks(fontsize=12, rotation=45, color='blue') # x-axis ticks
plt.yticks(fontsize=12, color='blue') # y-axis ticks

plt.show() # display the plot
