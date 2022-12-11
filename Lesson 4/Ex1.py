# Реализовать сортировку списка методом пузырька

from random import randint

# Creating and filling the list with 100 random values
amount = 100
list = []
for i in range(amount):
    list.append(randint(1, 999))

# Реализация 1
# Bubble sort
print("The list before bubble sort:", *list)
for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[j + 1] < list[j]:
            list[j + 1], list[j] = list[j], list[j + 1]
print("The list after bubble sort:", *list)


# Creating and filling the list with 100 random values
amount = 100
list = []
for i in range(amount):
    list.append(randint(1, 999))
    
# Реализация 2
# Bubble sort
print("The list before bubble sort:", *list)
for i in range(amount - 1):
    for j in range(amount - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print("The list after bubble sort:", *list)