'''
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
It is widely used for data visualization and provides a variety of plotting functions to create different types of charts and graphs.
In this file we will demonstrate a simple line plot using Matplotlib.
'''
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.use("TkAgg")

print(mpl.__version__)


x = np.array([2023, 2024, 2025, 2026])
y1= np.array([15, 25, 30, 20])
y2 = np.array([10, 30, 25, 15])
y3 = np.array([5, 15, 20, 10])

styles = {
    "line1": dict(
        marker='o',
        markersize=15,
        markerfacecolor="red",
        markeredgecolor="blue",
        linestyle="dashdot",
        linewidth=2,
        color="green"
    ),
    "line2": dict(
        marker='s',
        markersize=10,
        markerfacecolor="yellow",
        markeredgecolor="black",
        linestyle="dotted",
        linewidth=2,
        color="purple"
    ),
    "line3": dict(
        marker='^',
        markersize=8,
        markerfacecolor="orange",
        markeredgecolor="brown",
        linestyle="solid",
        linewidth=2,
        color="cyan"
    )
}

plt.plot(x, y1, **styles["line1"])
plt.plot(x, y2, **styles["line2"])
plt.plot(x, y3, **styles["line3"])

plt.xticks(x, fontsize=12, rotation=45, color='blue') # x-axis ticks
plt.yticks(fontsize=12, color='blue') # y-axis ticks



plt.title("Simple Line Plot with Three Lines", 
          fontsize = 20, 
          family = 'Arial', 
          fontweight = 'bold', 
          color = 'darkblue') # title of the plot


plt.xlabel("Year", 
           fontsize = 15, 
           family = 'Arial', 
           fontweight = 'bold', 
           color = 'darkgreen') # label for x-axis


plt.ylabel("Students Enrolled", 
           fontsize = 15, 
           family = 'Arial', 
           fontweight = 'bold', 
           color = 'darkred') # label for y-axis

plt.grid(True) # enable grid

plt.show() # show function to display the plot































