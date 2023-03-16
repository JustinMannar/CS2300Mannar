
def linear_map(src, tgt):
    # Compute the matrix A that transforms the source triangle to the
    # standard triangle with vertices (0, 0), (1, 0), and (0, 1).
    A = [
        [src[1][0] - src[0][0], src[2][0] - src[0][0]],
        [src[1][1] - src[0][1], src[2][1] - src[0][1]]
    ]
    detA = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    Ainv = [
        [A[1][1] / detA, -A[0][1] / detA],
        [-A[1][0] / detA, A[0][0] / detA]
    ]

    # Compute the matrix B that transforms the standard triangle to the
    # target triangle.
    B = [
        [tgt[1][0] - tgt[0][0], tgt[2][0] - tgt[0][0]],
        [tgt[1][1] - tgt[0][1], tgt[2][1] - tgt[0][1]]
    ]

    # Compute the matrix C that maps the source triangle to the target
    # triangle.
    C = [
        [Ainv[0][0] * B[0][0] + Ainv[0][1] * B[1][0], Ainv[0][0] * B[0][1] + Ainv[0][1] * B[1][1]],
        [Ainv[1][0] * B[0][0] + Ainv[1][1] * B[1][0], Ainv[1][0] * B[0][1] + Ainv[1][1] * B[1][1]]
    ]

    return C


tri1 = [(0,0),(1,0),(0,1)]
tri2 = [(1,0),(0,1),(0,0)]

print(linear_map(tri1,tri2))
