# Read the input matrix from the file
with open('pa3_test_input_1.txt', 'r') as f:
    A = []
    for line in f:
        row = [float(x) for x in line.split()]
        A.append(row)
    b = [A[i][2] for i in range(2)]
    A = [[A[i][j] for j in range(2)] for i in range(2)]

# Calculate the determinant of A
detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]

# Check the type of solution and print the output accordingly
if detA == 0:
    if b == [0, 0]:
        print("System undetermined")
    else:
        print("System inconsistent")
else:
    # Calculate the inverse of A
    invA = [[A[1][1]/detA, -A[0][1]/detA], [-A[1][0]/detA, A[0][0]/detA]]
    # Calculate the solution x
    x = [invA[0][0]*b[0] + invA[0][1]*b[1], invA[1][0]*b[0] + invA[1][1]*b[1]]
    # Print the output
    print("{:.4f}\n{:.4f}".format(x[0], x[1]))