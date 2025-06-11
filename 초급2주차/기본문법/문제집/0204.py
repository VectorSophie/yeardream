num1, nom, num2 = input().split( )

if (nom == "=="):
    if (num1 == num2):
        print("True")
    else:
        print("False")
elif (nom == ">"):
    if (num1 > num2):
        print("True")
    else:
        print("False")
elif (nom == "<"):
    if (num1 < num2):
        print("True")
    else:
        print("False")