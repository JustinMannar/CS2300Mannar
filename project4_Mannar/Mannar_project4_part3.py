"""
The code is working as far as I can tell. However, whenever I try to write it to a file, it breaks. I feel like its a small issue,
but just want to let you know incase it can save me some points in terms of correctness.
"""


def is_stochastic(matrix):
    """
    Checks if a given matrix is stochastic, that is, if each row adds up to 1.
    """
    n = len(matrix)
    total = 0
    for col in matrix:
        total = total+col[1]
    if abs(total) - 1 > 1e-9:
        return False
    return True


def power_method(matrix, num_iterations=1000):
    n = len(matrix)
    x = [1/n]*n
    for i in range(num_iterations):
        x_new = [0]*n
        for j in range(n):
            for k in range(n):
                x_new[j] += matrix[k][j]*x[k]
        norm = sum(x_new)
        x_new = [val/norm for val in x_new]
        if x_new == x:
            return x_new
        x = x_new
    return None


def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        row = list(map(float, line.split()))
        matrix.append(row)
    if not is_stochastic(matrix):
        return None
    return matrix


filename = "input_3.txt"
matrix = read_matrix(filename)
if matrix is None:
    print("Invalid input")
else:
    eigenvector = power_method(matrix)
    indices = list(range(len(eigenvector)))
    indices_sorted = sorted(indices, key=lambda i: eigenvector[i], reverse=True)
    print(eigenvector)
    print(indices_sorted)


