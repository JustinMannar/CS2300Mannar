print("Enter the elements of a 2x2 matrix:")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

det = a*d - b*c
mainSum = a + d
char_eqn = f"lambda^2 - {mainSum}*lambda + {det} = 0"
print("The characteristic equation is:", char_eqn)

lambda_1 = (mainSum + (mainSum ** 2 - 4 * det) ** 0.5) / 2
lambda_2 = (mainSum - (mainSum ** 2 - 4 * det) ** 0.5) / 2
print("The eigenvalues are:", lambda_1, "and", lambda_2)

if abs(lambda_1) > abs(lambda_2):
    dominantEV = lambda_1
else:
    dominantEV = lambda_2
print("The dominant eigenvalue is:", dominantEV)

if b != 0:
    eigenVector1 = [lambda_1 - d, b]
    eigenVector2 = [lambda_2 - d, b]
else:
    eigenVector1 = [b, lambda_1 - a]
    eigenVector2 = [b, lambda_2 - a]
print("The eigenvectors are:", eigenVector1, "and", eigenVector2)

# tested this code with an example from the book, the code got the right values
