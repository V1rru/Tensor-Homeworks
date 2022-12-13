# Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.

def sum(*args):
    list = []
    for arg in args:
        list.append(arg)
    for i in range(1, len(list)):
        list[0] += list[i]
    print(list[0])

sum(10, 20, 30, 40, 50, 60)
sum("Hello", ", ", "world!")
sum([1, 2, 3], [4, 5, 6])
sum((1, 2, 3), (4, 5, 6))
