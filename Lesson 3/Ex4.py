import math
import cmath

while True:

    # Choosing the way of calculating the equation
    choice = input("Choose between usual and compex coefficients (type usual/complex): ")

    if choice == "usual":
        # Getting coefficients
        print("Enter coefficients of the equation ax^2 + bx + c = 0")
        a = float(input("Enter a = "))
        b = float(input("Enter b = "))
        c = float(input("Enter c = "))

        # Calculating discriminant
        D = (b ** 2) - (4 * a * c)
        print("Discriminant =", D)

        # Calculating roots
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print(f'''x1 = {x1}
            x2 = {x2}''')
        elif D == 0:
            x = -b / (2 * a)
            print(f'''x = {x}''')
        elif D < 0:
            x1 = (-b + cmath.sqrt(D)) / (2 * a)
            x2 = (-b - cmath.sqrt(D)) / (2 * a)
            print(f'''x1 = {x1}''')
            print(f'''x2 = {x2}''')
        break
    
    elif choice == "complex":
        # Getting coefficients
        print("Enter complex coefficients of the equation ax^2 + bx + c = 0")
        aReal = float(input("Enter a (real) = "))
        aImag = float(input("Enter a (imag) = "))
        bReal = float(input("Enter b (real) = "))
        bImag = float(input("Enter b (imag) = "))
        cReal = float(input("Enter c (real) = "))
        cImag = float(input("Enter c (imag) = "))

        a = complex(aReal, aImag)
        b = complex(bReal, bImag)
        c = complex(cReal, cImag)

        # Calculating discriminant
        D = (b ** 2) - (4 * a * c)
        print("Discriminant =", D)

        # Calculating roots
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        print(f'''x1 = {x1}''')
        print(f'''x2 = {x2}''')
        break

    else: 
        print("Wrong word. Try again")


