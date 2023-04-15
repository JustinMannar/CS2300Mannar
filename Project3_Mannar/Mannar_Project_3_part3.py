# Open the input file
with open("3D_test_input_1.txt") as f:
    # Read the first line to determine if the matrix is 2x3 or 3x3
    first_line = f.readline().strip()
    is_2d = (len(first_line.split()) == 4)

    # Read the matrix
    matrix = []
    for line in f:
        row = [float(x) for x in line.strip().split()]
        matrix.append(row)

    # Extract the point coordinates
    if is_2d:
        x1, y1, x2, y2, x3, y3 = matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[1][0], matrix[1][1]
    else:
        x1, y1, z1, x2, y2, z2, x3, y3, z3 = matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[0][4], matrix[0][5], matrix[1][0], matrix[1][1], matrix[1][2]

    # Compute the area of the triangle
    if is_2d:
        area = abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
    else:
        area = abs((x1*(y2*z3-y3*z2)+x2*(y3*z1-y1*z3)+x3*(y1*z2-y2*z1))/2)

    # Compute the distance between the third point and the line/plane formed by the first two points
    if is_2d:
        # Compute the slope and intercept of the line
        if x2 == x1:
            slope = float("inf")
        else:
            slope = (y2-y1)/(x2-x1)
        intercept = y1 - slope*x1

        # Compute the distance between the third point and the line
        distance = abs(slope*x3 - y3 + intercept)/((1 + slope**2)**0.5)
    else:
        # Compute the normal vector of the plane
        v1 = [x2-x1, y2-y1, z2-z1]
        v2 = [x3-x1, y3-y1, z3-z1]
        normal = [v1[1]*v2[2]-v1[2]*v2[1], v1[2]*v2[0]-v1[0]*v2[2], v1[0]*v2[1]-v1[1]*v2[0]]

        # Compute the distance between the third point and the plane
        distance = abs(normal[0]*x3 + normal[1]*y3 + normal[2]*z3 - (normal[0]*x1 + normal[1]*y1 + normal[2]*z1))/((normal[0]**2 + normal[1]**2 + normal[2]**2)**0.5)

    # Output the results with 4 decimal places
    print("{:.4f}".format(area))
    print("{:.4f}".format(distance))
