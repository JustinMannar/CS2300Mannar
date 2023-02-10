m1 = [[], [], [], [], [], []]
matrix1 = open('jmannar_mat1.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m1[i].append(float(num))
    i = i + 1
#print(m1)

#print("\n")

m2 = [[], [], [], [], [], []]
matrix1 = open('jmannar_mat2.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m2[i].append(float(num))
    i = i + 1
#print(m2)

#print("\n")

m3 = [[], [], [], [], [], []]
matrix1 = open('jmannar_mat3.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m3[i].append(float(num))
    i = i + 1
#print(m3)

#print("\n")

m4 = [[], [], [], []]
matrix1 = open('jmannar_mat4.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m4[i].append(float(num))
    i = i + 1
#print(m4)

#print("\n")

m5 = [[], [], [], []]
matrix1 = open('jmannar_mat5.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m5[i].append(float(num))
    i = i + 1
#print(m5)

#print("\n")

m6 = [[], []]
matrix1 = open('jmannar_mat6.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m6[i].append(float(num))
    i = i + 1
#print(m6)

def addMatrices(matrix1, matrix2):
    sumMatrix = [[0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0],
                 [0,0,0,0,0,0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            sumMatrix[i][j] = matrix1[i][j]+matrix2[i][j]
            print(sumMatrix[i][j])


addMatrices(m1, m2)