num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

operand = input("Введите операнд (+, -, *, /): ")


if operand == '+':
    print(f"Результат: {num1} + {num2} = {num1 + num2}")
elif operand == '-':
    print(f"Результат: {num1} - {num2} = {num1 - num2}")
elif operand == '*':
    print(f"Результат: {num1} * {num2} = {num1 * num2}")
elif operand == '/':
    if num2 != 0:
        print(f"Результат: {num1} / {num2} = {num1 / num2}")
    else:
        print("Ошибка: Деление на ноль невозможно.")
else:
    print("Ошибка: Неверный операнд. Используйте +, -, *, /.")
