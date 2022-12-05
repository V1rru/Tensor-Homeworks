

# Start coordinates
Coords = [0, 0]
print("Start position (X Y): ", *Coords)

# Getting the user's choice
choice = input("Enter direction (up/down/right/left): ").lower()

# Different variants of commands
if choice == "up":
    Coords[1] += 1
    print("Current position (X Y): ", *Coords)
elif choice == "down":
    Coords[1] -= 1
    print("Current position (X Y): ", *Coords)
elif choice == "right":
    Coords[0] += 1
    print("Current position (X Y): ", *Coords)
elif choice == "left":
    Coords[0] -= 1
    print("Current position (X Y): ", *Coords)
else:
    print("Wrong comand, try again using up/down/right/left")