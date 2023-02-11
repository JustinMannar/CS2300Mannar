d = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], ]

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for k in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][k])
        matrix_T.append(row)

    return matrix_T

def writeFile(matrix, file):
    with open(file, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda n: f"{n:.2f}", row)) + '\n')


m1 = [[], [], [], [], [], []]
matrix1 = open('jmannar_mat1.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m1[i].append(float(num))
    i = i + 1

# print(m1)
t1 = transpose(m1)
print(t1)
writeFile(t1, "jmannar_p6_mat1.txt")

print("\n")

m2 = [[], [], [], [], [], []]
matrix2 = open('jmannar_mat2.txt', 'r')
i = 0

for line in matrix2.readlines():
    l = line.split(" ")
    for num in l:
        m2[i].append(float(num))
    i = i + 1

t2 = transpose(m2)
print(t2)
writeFile(t2, "jmannar_p6_mat2.txt")

print("\n")

m3 = [[], [], [], [], [], []]
matrix3 = open('jmannar_mat3.txt', 'r')
i = 0

for line in matrix3.readlines():
    l = line.split(" ")
    for num in l:
        m3[i].append(float(num))
    i = i + 1

t3 = transpose(m3)
print(t3)
writeFile(t3, "jmannar_p6_mat3.txt")

print("\n")

m4 = [[], [], [], []]
matrix4 = open('jmannar_mat4.txt', 'r')
i = 0

for line in matrix4.readlines():
    l = line.split(" ")
    for num in l:
        m4[i].append(float(num))
    i = i + 1

m5 = [[], [], [], []]
matrix5 = open('jmannar_mat5.txt', 'r')
i = 0

for line in matrix5.readlines():
    l = line.split(" ")
    for num in l:
        m5[i].append(float(num))
    i = i + 1

t4 = transpose(m4)
print(t4)
writeFile(t4, "jmannar_p6_mat4.txt")

print('\n')

t5 = (transpose(m5))
print(t5)

writeFile(t5, "jmannar_p6_mat5.txt")

print('\n')

m6 = [[], []]
matrix6 = open('jmannar_mat6.txt', 'r')
i = 0

for line in matrix6.readlines():
    l = line.split(" ")
    for num in l:
        m6[i].append(float(num))
    i = i + 1

t6 = transpose(m6)
print(t6)

writeFile(t6, "jmannar_p6_mat6_txt")
