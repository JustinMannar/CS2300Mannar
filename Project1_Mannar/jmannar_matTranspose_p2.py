d = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], ]

d_2 = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]


def writeFile(matrix, file):
    with open(file, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda n: f"{n:.2f}", row)) + '\n')


# m1
m1 = [[], [], [], [], [], []]
matrix1 = open('jmannar_mat1.txt', 'r')
i = 0

for line in matrix1.readlines():
    l = line.split(" ")
    for num in l:
        m1[i].append(float(num))
    i = i + 1

# print(m1)

# m2
for i in range(len(m1)):
    # iterate through columns
    for j in range(len(m1[0])):
        d[j][i] = m1[i][j]
for r in d:
    print(r)

print("\n")

m2 = [[], [], [], [], [], []]
matrix2 = open('jmannar_mat2.txt', 'r')
i = 0

for line in matrix2.readlines():
    l = line.split(" ")
    for num in l:
        m2[i].append(float(num))
    i = i + 1

for i in range(len(m2)):
    # iterate through columns
    for j in range(len(m2[0])):
        d[j][i] = m2[i][j]
for r in d:
    print(r)

print("\n")
# m3

m3 = [[], [], [], [], [], []]
matrix3 = open('jmannar_mat3.txt', 'r')
i = 0

for line in matrix3.readlines():
    l = line.split(" ")
    for num in l:
        m3[i].append(float(num))
    i = i + 1

for i in range(len(m3)):
    # iterate through columns
    for j in range(len(m3[0])):
        d[j][i] = m3[i][j]
for r in d:
    print(r)

print("\n")

m4 = [[]]*4
matrix4 = open('jmannar_mat4.txt', 'r')
i = 0

for line in matrix4.readlines():
    l = line.split(" ")
    for num in l:
        m4[i].append(float(num))
    i = i + 1
print(m4)
for i in range(len(m4)):
    # iterate through columns
    for j in range(len(m4[0])):
        d_2[j][i] = m4[i][j]
for r in d_2:
    print(r)

print("\n")
"""
m5 = []
matrix5 = open('jmannar_mat5.txt', 'r')
i = 0

for line in matrix5.readlines():
    l = line.split(" ")
    for num in l:
        m5[i].append(float(num))
    i = i + 1

for i in range(len(m5)):
    # iterate through columns
    for j in range(len(m5[0])):
        d_2[j][i] = m5[i][j]
for r in d_2:
    print(r)
"""

