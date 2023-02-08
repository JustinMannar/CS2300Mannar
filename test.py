def makeMatrix (nrows, ncols, start, incr):
    mat = []

    for i in range(0, nrows, 1):
        mat.append([])
        for j in range(0, ncols, 1):
            mat[i].append(start)
            start = start + incr
    for i in range(0, nrows, 1):
        print(mat[i][0], mat[i][1], mat[i][2], mat[i][3], mat[i][4], mat[i][5])
    return mat

def writeToFile(matrix,file):
    f=open(file,"a")
    f.write(matrix)
    f.close()


print(makeMatrix(6, 6, 1, 1))

print(makeMatrix(6, 6, 2, 3))

print(makeMatrix(6, 6, 0.2, 0.2))

print(makeMatrix(4, 6, 10, -2))

print(makeMatrix(4, 6, -6, 1.5))

#print(makeMatrix(2,4,-10,10))





