firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
if float(firstNumber).is_integer():
    firstNumber = int(firstNumber)
if float(secondNumber).is_integer():
    secondNumber = int(secondNumber)
sum = firstNumber + secondNumber
sub = firstNumber - secondNumber
mult = firstNumber * secondNumber
div = firstNumber / secondNumber
pow = firstNumber ** secondNumber
mod = firstNumber % secondNumber
idiv = firstNumber // secondNumber
print(f'''First number: {firstNumber},
Second number: {secondNumber},
Sum: {sum},
Subtraction (first - second): {sub},
Multiplication: {mult},
Division (first / second): {div},
Power (first ** second): {pow},
Division by mod (first mod second): {mod},
Int division (first div second): {idiv} ''')