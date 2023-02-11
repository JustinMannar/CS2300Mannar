def vecSubtract(vector01, vector02):
    result = [vector01[i] - vector02[i] for i in range(min(len(vector01), len(vector02)))]
    return result

vector01 = [2, -1]
vector02 = [3, 1]

subvec = vecSubtract(vector01, vector02)
print(subvec)

def vecAdd(vector01, vector02):
    result = [vector01[i] + vector02[i] for i in range(min(len(vector01), len(vector02)))]
    return result


v2_1 = [-1, -2]
v2_2 = [-3, 3]
v2_3 = [1, 3]

addVec1 = vecAdd(v2_1, v2_2)
addVec2 = vecAdd(v2_2, v2_3)

print(addVec1)
print(addVec2)