# Создать игровой инвентарь. 
# Должна быть возможность добавлять в него предметы и удалять предметы из него. 
# Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес. Вывод предметов должен быть с названием предмета и его весом.

inventory = {"sword": 10, "shield": 15}
maxWeight = 100

while True:
    # Counting items and their weights
    totalWeight = 0
    for value in inventory.values():
        totalWeight += value

    print(f'''Now your inventory has {len(inventory)} items with total weight of {totalWeight}''')
    print("The whole inventory is:", *inventory.items())
    choice = (input("Choose what you want to do with your inventory: add an item (add), remove an item (remove) or stop working with the inventory (stop): "))
    
    if choice == "add":
        item = input("Enter the denomination and integer weight of an item (denomination weight: sword 10): ").split()
        if (int(item[1]) + totalWeight) <= maxWeight:
            inventory.update({item[0]: int(item[1])})
        else: 
            print("Sorry, there is no place for this item")
    elif choice == "remove":
        item = input("Enter the denomination of an item that you want to remove: ")
        result = inventory.pop(item, "Sorry, there is no such item")
        if result == "Sorry, there is no such item":
            print("Sorry, there is no such item")
        else:
            print(item, "successfully removed")
    elif choice == "stop":
        break
    else:
        print("Sorry, unknown command")