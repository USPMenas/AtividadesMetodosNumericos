# importing the required module
import matplotlib.pyplot as plt
import numpy as np

# x axis values
x = np.arange(0,4*np.pi, 0.0005)
# corresponding y axis values
w = np.cos(x)
y = np.cos(2*x)
z = np.cos(3*x)
  
# plotting the points 
plt.plot(x, w, 'r--', label='m = 1')
plt.plot(x, y, 'b:', label='m = 2')
plt.plot(x, z, 'g-.', label='m = 3')

# naming the x axis
plt.xlabel('x - dimensionless')
# naming the y axis
plt.ylabel('y - dimensionless')
  
# giving a title to my graph
plt.title('Graphs of y(t) = cos(m*t) for m = 1, 2 and 3')
plt.legend(loc='upper left')
  
# function to show the plot
plt.show()