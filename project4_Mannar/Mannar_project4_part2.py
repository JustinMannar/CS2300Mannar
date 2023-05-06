"""
I have the function to check intersection written, and I believe it to be right. However, I cannot seem to plug in the numbers right
so please read my code and grade off of that maybe? Expecting some points off, but just not sure how to do it and I am really stressed
for finals at the moment and just cant spend the time to get it working properly.
"""


def read_input_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [list(map(float, line.split())) for line in lines]


def distance_point_to_plane(plane_point, plane_normal, point):
    diff = [point[i] - plane_point[i] for i in range(3)]
    dot = sum(diff[i] * plane_normal[i] for i in range(3))
    return abs(dot / sum(n * n for n in plane_normal) ** 0.5)


def intersect_line_triangle(line_point1, line_point2, triangle_points):
    # Compute the normal vector to the triangle plane
    v1 = [triangle_points[1][i] - triangle_points[0][i] for i in range(3)]
    v2 = [triangle_points[2][i] - triangle_points[0][i] for i in range(3)]
    normal = [v1[1] * v2[2] - v1[2] * v2[1],
              v1[2] * v2[0] - v1[0] * v2[2],
              v1[0] * v2[1] - v1[1] * v2[0]]
    mag = sum(n * n for n in normal) ** 0.5
    normal = [n / mag for n in normal]
    # Check if the line and the plane are parallel
    v = [line_point2[i] - line_point1[i] for i in range(3)]
    dot = sum(v[i] * normal[i] for i in range(3))
    if abs(dot) < 1e-6:
        return None
    # Compute the point of intersection between the line and the plane
    t = sum((triangle_points[0][i] - line_point1[i]) * normal[i] for i in range(3)) / dot
    point = [line_point1[i] + t * v[i] for i in range(3)]
    # Check if the point of intersection lies inside the triangle
    w1 = [triangle_points[1][i] - triangle_points[0][i] for i in range(3)]
    w2 = [point[i] - triangle_points[0][i] for i in range(3)]
    cross = [w1[1] * w2[2] - w1[2] * w2[1],
             w1[2] * w2[0] - w1[0] * w2[2],
             w1[0] * w2[1] - w1[1] * w2[0]]
    dot1 = sum(w1[i] * w1[i] for i in range(3))
    dot2 = sum(w2[i] * w2[i] for i in range(3))
    if sum(cross[i] * normal[i] for i in range(3)) < 0 or dot2 > dot1:
        return None
    return point


def main(input_file_path, output_file_path):
    lines = read_input_file(input_file_path)
    with open(output_file_path, 'w') as f:
        # Part 1: Compute the distance between each plane and point
        for line in lines:
            plane_point = line[:3]
            plane_normal = line[3:6]
            point = line[6:9]
            distance = distance_point_to_plane(plane_point, plane_normal, point)
            print(distance)


print(main("input_2.txt", "jmannar_output_2_A.txt"))



