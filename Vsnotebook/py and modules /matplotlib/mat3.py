'''
In this file we are going to learn how to create pie chart using matplotlib
'''

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.use("TkAgg")

labels = np.array(["Python", "JavaScript", "C++", "Java", "Ruby"])
sizes = np.array([40, 25, 15, 10, 10])
explode = np.array([0.1, 0, 0, 0, 0])  # explode the 1st slice (Python), it means offset it from the center

plt.title("Programming Language Popularity", 
          fontsize = 20, 
          family = 'Arial', 
          fontweight = 'bold', 
          color = 'darkblue') # title of the plot     



plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        # startangle=140,
        colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'violet'],
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})      

plt.show()  # display the plot