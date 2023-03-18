
def linear_map(src, tgt):
    a = [
        [src[1][0] - src[0][0], src[2][0] - src[0][0]],
        [src[1][1] - src[0][1], src[2][1] - src[0][1]]
    ]
    detA = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    Ainv = [
        [a[1][1] / detA, -a[0][1] / detA],
        [-a[1][0] / detA, a[0][0] / detA]
    ]

    b = [
        [tgt[1][0] - tgt[0][0], tgt[2][0] - tgt[0][0]],
        [tgt[1][1] - tgt[0][1], tgt[2][1] - tgt[0][1]]
    ]

    c = [
        [Ainv[0][0] * b[0][0] + Ainv[0][1] * b[1][0], Ainv[0][0] * b[0][1] + Ainv[0][1] * b[1][1]],
        [Ainv[1][0] * b[0][0] + Ainv[1][1] * b[1][0], Ainv[1][0] * b[0][1] + Ainv[1][1] * b[1][1]]
    ]

    return c


tri1 = [(0, 1), (-1, -1), (1, -1)]
tri2 = [(0, 1), (1, 3), (-1, 3)]        # an example from the book, calculates it correctly

print(linear_map(tri1, tri2))
