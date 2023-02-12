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


def writeFile(matrix, file):
    with open(file,'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda n: f"{n:.2f}", row)) + '\n')


def multiplyMatrices(mat1, mat2):
    result = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    for r in result:
        print(r)

def multiplySmallerMatrices(mat1, mat2):
    result = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    for r in result:
        print(r)


mult1 = multiplyMatrices(m1,m2)
print('\n')
mult2 = multiplyMatrices(m1,m3)
print('\n')
mult3 = multiplyMatrices(m2,m3)
print('\n')
mult4 = multiplySmallerMatrices(m4,m5)
print('\n')
mult5 = multiplySmallerMatrices(m4,m6)
print('\n')
mult6 = multiplySmallerMatrices(m5,m6)
print('\n')
mult7 = multiplySmallerMatrices(m6,m5)
print('\n')
mult8 = multiplySmallerMatrices(m6,m4)
print('\n')
mult9 = multiplySmallerMatrices(m5,m4)
print('\n')
mult10 = multiplyMatrices(m3,m2)
print('\n')
mult11 = multiplyMatrices(m3,m1)
print('\n')
mult12 = multiplyMatrices(m2,m1)

"""
Above is every instance where two of the matrices can be multiplied together. 
I was unable to make a function that called for user input and wrote the output to a file. I ran into similar 
problems with adding matrices, but I showed that every possible add matrix was created there as well. 
"""

