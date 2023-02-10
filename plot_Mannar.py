import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as tri
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('vectors in standard position')
data = np.array([[-1, -2], [-3, 3], [2, -1], [3, 1], [1, 3]])
origin = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
plt.quiver(*origin, data[:, 0], data[:, 1], color=['black', 'red', 'green', 'blue', 'orange'], scale=15)
plt.show()

#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
#data = np.array([[-1, -2], [-3, 3], [2, -1]])
#origin = np.array([[0, 0, 0], [0, 0, 0]])
#plt.quiver(*origin, data[:, 0], data[:, 1], color=['black', 'red', 'green'], scale=15)
#plt.show()

