firstName = 'Justin'
lastName = 'Mannar'
def makeMatrix (nrows, ncols, start, incr):
    mat = []

    for i in range(0, nrows, 1):
        mat.append([])
        for j in range(0, ncols, 1):
            mat[i].append(start)
            start = start + incr
    for i in range(0, nrows, 1):
        for j in range(0,ncols,1):
            #print(mat[i][j])
            j = j+1

    return mat


def writeFile(matrix, file):
    with open(file,'w') as f:
        for row in matrix:
            f.write(' '.join(map(lambda n: f"{n:.2f}", row)) + '\n')


mat1 = (makeMatrix(len(firstName), len(lastName), 1, 1))
print(mat1)
writeFile(mat1,"jmannar_mat1.txt")

mat2 = (makeMatrix(len(firstName), len(lastName), 2, 3))
print(mat2)
writeFile(mat2,"jmannar_mat2.txt")

mat3 = (makeMatrix(len(firstName), len(lastName), 0.2, 0.2))
print(mat3)
writeFile(mat3,"jmannar_mat3.txt")

mat4 = (makeMatrix(4, 6, 10, -2))
print(mat4)
writeFile(mat4,"jmannar_mat4.txt")

mat5 = (makeMatrix(4, 6, -6, 1.5))
print(mat5)
writeFile(mat5,"jmannar_mat5.txt")

mat6 = (makeMatrix(2,4,-10,10))
print(mat6)
writeFile(mat6,"jmannar_mat6.txt")




