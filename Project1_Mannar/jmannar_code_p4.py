def dot(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))


def writeFile(row, file):
    with open(file,'w') as f:
            f.write(' '.join(map(lambda n: f"{n:.2f}", row)) + '\n')


dot1_1 = [-1, -2]
dot1_2 = [-3, 3]

dot2_1 = [2, -1]
dot2_2 = [3, 1]

dot3_1 = [-3, 3]
dot3_2 = [3, 1]

dot1 = dot(dot1_1, dot1_2)
print(dot1)
writeFile([dot1], "jmannar_p4_rs.txt")

dot2 = dot(dot2_1, dot2_2)
print(dot2)
writeFile([dot2], "jmannar_p4_uv.txt")

dot3 = dot(dot3_1, dot3_2)
print(dot3)
writeFile([dot3], "jmannar_p4_sv.txt")