# Ask the user for the equation form
print("Enter the equation you would like to convert: ")
print("i - Implicit (ax + by + c = 0)")
print("p - Parametric (p + tv)")
userChoice = input("Enter i or p: ")

if userChoice == "i":
    print("please enter the value for a:")
    a = float(input())
    print("please enter the value for b:")
    b = float(input())
    print("please enter the value for c:")
    c = float(input())

    v = [b, a * -1]

    if abs(a) > abs(b):
        newValue = [c/(a * -1), 0]
        print(newValue)
    elif abs(a) <= abs(b):
        newValue = [0, c/(b * -1)]
        print(newValue)

    print("parametric equation  is: l(t) = (" + str(newValue[0]) + "," + str(newValue[1])+") + t(" + str(v[0]) + "," + str(v[1])+")")

elif userChoice == "p":
    print("enter first value of point p:")
    p1 = float(input())
    print("enter second value of point p:")
    p2 = float(input())

    point = [p1, p2]

    print("enter first element of vector v:")
    v1 = float(input())
    print("enter second element of vector v:")
    v2 = float(input())

    vector = [v1, v2]
    ngt = vector[1] * -1
    newVector = [ngt, vector[0]]

    impA = newVector[0]
    impB = newVector[1]
    impC = ((point[0] * impA) + (point[1] * impB)) * -1

    print("the implicit equation is: " + str(impA) + "x1 + " + str(impB) + "x2 + " + str(impC) + " = 0")

else:
    print("not a valid entry, please try the program again and enter either i or p")
