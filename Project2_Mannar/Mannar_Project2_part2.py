
def multiply_matrices(a, b):
    # Create a new 2x2 matrix C to hold the product
    c = [[0.0, 0.0], [0.0, 0.0]]

    # Multiply the matrices element-wise
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] += a[i][k] * b[k][j]

    return c


row = 2
col = 2
Identity = [[1.0, 0.0], [0.0, 1.0]]

A = []
for i in range(row):
    I = []
    for j in range(col):
        v = float(input('please enter value: '))
        I.append(v)
    A.append(I)
print(A)

# Check if inverse exists
detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
if detA == 0:
    print("The matrix does not have an inverse.")
else:
    s1 = [[1.0, 0.0], [round((-1*(A[1][0]))/A[0][0], 2), 1.0]]
    inverse1A = multiply_matrices(s1, A)
    inverse1B = multiply_matrices(s1, Identity)

    s2 = [[1.0, round((-1*(A[0][1])/A[1][1]), 2)], [0.0, 1.0]]
    inverse2A = multiply_matrices(s2, inverse1A)
    inverse2B = multiply_matrices(s2, inverse1B)

    s3 = [[round(1/inverse2A[0][0], 2), 0.0], [0.0, round(1/inverse2A[1][1], 2)]]
    inverse3A = multiply_matrices(s3, inverse2A)
    inverse3B = multiply_matrices(s3, inverse2B)

    print("the inverse matrix is:")
    print(inverse3B)
