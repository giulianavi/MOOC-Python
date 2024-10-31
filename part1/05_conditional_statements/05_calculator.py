number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

multiplicacao = number1 * number2
adicao = number1 + number2
subtracao = number1 - number2

if operation == 'multiply':
    print(f"{number1} * {number2} = {multiplicacao}")
if operation == 'add':
    print(f"{number1} + {number2} = {adicao}")
if operation == 'subtract':
    print(f"{number1} - {number2} = {subtracao}")