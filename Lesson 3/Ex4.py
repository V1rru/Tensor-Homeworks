import math

while True:
    # Choosing the way of calculating the equation
    choice = input("Choose between usual and compex coefficients (type usual/complex): ")
    if choice == "usual":
        # Getting coefficients
        print("Enter coefficients of the equation ax^2 + bx + c = 0")
        a = float(input("Enter a = "))
        b = float(input("Enter b = "))
        c = float(input("Enter c = "))
        break
    elif choice == "complex":
        # Getting coefficients


        ################# ПЕРЕДЕЛАТЬ #################
        print("Enter coefficients of the equation ax^2 + bx + c = 0")
        a = float(input("Enter a = "))
        b = float(input("Enter b = "))
        c = float(input("Enter c = "))
        ################# ПЕРЕДЕЛАТЬ #################


        break
    else: 
        print("Wrong word. Try again")


# Calculating discriminant
D = (b ** 2) - (4 * a * c)
print("Discriminant = ", D)

# Calculating roots
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f'''x1 = {x1}
    x2 = {x2}''')
elif D == 0:
    x = -b / (2 * a)
    print(f'''x = {x}''')
else:
    print(f'''The equation has no roots''')