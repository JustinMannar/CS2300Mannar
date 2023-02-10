import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as tri
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True
#plt.xlabel('x-axis')
#plt.ylabel('y-axis')
#plt.title('vectors in standard position')
#data = np.array([[-1, -2], [-3, 3], [2, -1], [3, 1], [1, 3]])
#origin = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
#plt.quiver(*origin, data[:, 0], data[:, 1], color=['black', 'red', 'green', 'blue', 'orange'], scale=15)
#plt.show()


def dot(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))


def writeFile(row, file):
    with open(file,'w') as f:
            f.write(' '.join(map(lambda n: f"{n:.2f}", row)) + '\n')


dot1_1 = [-1, -2]
dot1_2 = [-3, 3]

dot2_1 = [2, -1]
dot2_2 = [3, 1]

dot3_1 = [-3, 3]
dot3_2 = [3, 1]

dot1 = dot(dot1_1, dot1_2)
#print(dot1)
writeFile([dot1], "jmannar_p4_rs.txt")

dot2 = dot(dot2_1, dot2_2)
#print(dot2)
writeFile([dot2], "jmannar_p4_uv.txt")

dot3 = dot(dot3_1, dot3_2)
#print(dot3)
writeFile([dot3], "jmannar_p4_sv.txt")

def vecSubtract(vector01, vector02):
    result = [vector01[i] - vector02[i] for i in range(min(len(vector01), len(vector02)))]
    return result

vector01 = [2, -1]
vector02 = [3, 1]

subVec = vecSubtract(vector01, vector02)
#print(subVec)

def vecAdd(vector01, vector02):
    result = [vector01[i] + vector02[i] for i in range(min(len(vector01), len(vector02)))]
    return result


v2_1 = [-1, -2]
v2_2 = [-3, 3]
v2_3 = [1, 3]

addVec1 = vecAdd(v2_1, v2_2)
addVec2 = vecAdd(v2_2, v2_3)

#print(addVec1)
#print(addVec2)

plt.rcParams["figure.figsize"] = [9.00, 7.50]
plt.rcParams["figure.autolayout"] = True
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('vectors in standard position')
data = np.array([addVec1, addVec2, subVec])
origin = np.array([[0, 0, 0], [0, 0, 0]])
plt.quiver(*origin, data[:, 0], data[:, 1], color=['yellow', 'red', 'green'], scale=15)
plt.show()

