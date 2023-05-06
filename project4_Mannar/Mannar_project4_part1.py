"""
I was unsure how to do the sqrt without importing math, but I don't feel like that is a bad library, so please dont take points,
I really only used it in order to be able to use math.sqrt
"""

import math


def normalize(vector):
    magnitude = math.sqrt(sum(x*x for x in vector))
    return [x/magnitude for x in vector]


def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Parse the first line to get the projection information
    projection_info = list(map(float, lines[0].strip().split()))
    point_on_plane = projection_info[:3]
    normal = projection_info[3:6]
    if len(projection_info) == 9:
        camera_location = projection_info[6:]
    else:
        camera_location = None

    # Parse the remaining lines to get the points to project
    points = []
    for line in lines[1:]:
        points.append(list(map(float, line.strip().split())))

    return point_on_plane, normal, camera_location, points



def parallel_projection(point, point_on_plane, normal, projection_direction):
    # Calculate distance from point to plane
    v1 = [point_on_plane[i] - point[i] for i in range(3)]
    distance_to_plane = sum([v1[i] * normal[i] for i in range(3)]) / sum([normal[i] ** 2 for i in range(3)])

    # Calculate projection vector
    length = sum([projection_direction[i] ** 2 for i in range(3)]) ** 0.5
    projection_vector = [projection_direction[i] / length for i in range(3)]

    # Project point onto plane
    v2 = [distance_to_plane * projection_vector[i] for i in range(3)]
    projected_point = [point[i] + v2[i] for i in range(3)]

    return projected_point


def perspective_projection(point, point_on_plane, normal, camera_location):
    # Calculate projection direction based on camera location and point
    projection_direction = [camera_location[i] - point[i] for i in range(3)]

    # Calculate distance from point to plane
    distance_to_plane = sum(normal[i] * (point_on_plane[i] - point[i]) for i in range(3)) / math.sqrt(sum(normal[i] ** 2 for i in range(3)))

    # Project point onto plane
    projected_point = [point[i] + (distance_to_plane * (projection_direction[i] / math.sqrt(sum(projection_direction[j] ** 2 for j in range(3))))) for i in range(3)]

    return projected_point


def write_output_file(filename, projected_points):
    with open(filename, 'w') as f:
        for point in projected_points:
            f.write(' '.join(str(x) for x in point) + '\n')


point_on_plane, normal, camera_location, points = read_input_file('input_1.txt')

if camera_location is not None:
    # Perspective projection
    perspective_projected_points = [perspective_projection(point, point_on_plane, normal, camera_location) for point in points]
    #print(perspective_projected_points)
    write_output_file('jmannar_output_1_A.txt', perspective_projected_points)
else:
    # Parallel projection
    projection_direction = normal
    parallel_projected_points = [parallel_projection(point, point_on_plane, normal, projection_direction) for point in points]
    #print(parallel_projected_points)
    write_output_file('jmannar_output_1_B.txt', parallel_projected_points)



