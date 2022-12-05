
# Start coordinates
Coords = [0, 0]
print("Start position (X Y): ", *Coords)

# Getting the user's choice
print("If you want to exit, type 'stop'")
choice = input("Enter direction (up/down/right/left): ").lower()

# Different variants of commands
while choice != "stop":
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

    choice = input("Enter direction (up/down/right/left): ").lower()

print("Stopped. The final position is (X Y): ", *Coords)