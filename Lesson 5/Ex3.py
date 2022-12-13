# Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия)

def fib(amount):
    if (amount == 1 or amount == 2):
        return 1
    return fib(amount - 1) + fib(amount - 2)

number = input("Enter an integer number: ")

if number.isnumeric() == True:
    number = int(number)
    print("Your current Fibonacci number is:", fib(number))
else:
    print("You entered the wrong value")
