# Read the input matrix from the file
with open('test_input_2.txt', 'r') as f:
    A = [[float(num) for num in line.split()] for line in f]

# Compute the determinant and trace of A
det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
trace_A = A[0][0] + A[1][1]

# Compute the discriminant of the characteristic polynomial of A
discriminant = trace_A**2 - 4*det_A

if discriminant >= 0:
    # Compute the eigenvalues of A
    lambda1 = (trace_A + (discriminant)**0.5)/2
    lambda2 = (trace_A - (discriminant)**0.5)/2

    # Compute the eigenvectors of A
    if A[0][1] != 0:
        eigenvector1 = [lambda1 - A[1][1], A[0][1]]
        eigenvector2 = [lambda2 - A[1][1], A[0][1]]
    elif A[1][0] != 0:
        eigenvector1 = [A[1][0], lambda1 - A[0][0]]
        eigenvector2 = [A[1][0], lambda2 - A[0][0]]
    else:
        eigenvector1 = [1, 0]
        eigenvector2 = [0, 1]

    # Normalize the eigenvectors
    norm1 = (eigenvector1[0]**2 + eigenvector1[1]**2)**0.5
    norm2 = (eigenvector2[0]**2 + eigenvector2[1]**2)**0.5
    eigenvector1 = [eigenvector1[0]/norm1, eigenvector1[1]/norm1]
    eigenvector2 = [eigenvector2[0]/norm2, eigenvector2[1]/norm2]

    # Create the diagonal matrix of eigenvalues
    Lambda = [[lambda1, 0], [0, lambda2]]

    # Create the matrix R of eigenvectors
    R = [eigenvector1, eigenvector2]

    # Compute the matrix composition RΛRT
    R_lambda_Rt = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                R_lambda_Rt[i][j] += R[i][k] * Lambda[k][j]
            R_lambda_Rt[i][j] *= R[j][k]

    # Print the output
    for i in range(2):
        print("{:.4f} {:.4f}".format(Lambda[i][i], 0))
    for i in range(2):
        print("{:.4f} {:.4f}".format(R[0][i], R[1][i]))
    for i in range(2):
        print("{:.4f} {:.4f}".format(R_lambda_Rt[i][0], R_lambda_Rt[i][1]))

else:
    print("No real eigenvalues")
