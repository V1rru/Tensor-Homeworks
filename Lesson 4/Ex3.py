# Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
# входят одновременно в оба;
# входят только в первое, но не входят во второе;
# входят только во второе, но не входят в первое;
# входят в первое или во второе, но не в оба из них одновременно.

from random import randint

# Creating and filling the sets with 10 random values
set1 = {randint(1,9) for i in range(10)}
set2 = {randint(1,9) for i in range(10)}
print("The first set before operations:", set1)
print("The second set before operations:", set2)

print("Elements same for both sets:", set1.intersection(set2))
print("Elements unique for the first set:", set1.difference(set2))
print("Elements unique for the second set:", set2.difference(set1))
print("Elements unique for the first or second set, but not for both directly:", set1.symmetric_difference(set2))