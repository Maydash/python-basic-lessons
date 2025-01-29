# Условные операторы if, else, elif в Python

# if условие:
    # код выполняется, если условие True
# elif другое_условие:
    # код выполняется, если первое False, но это True
# else:
    # код выполняется, если все условия False

num = 10

if num > 0:
    print("Число положительное")
elif num < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")


login = "admin"
password = "1234"

if login == "admin" and password == "1234":
    print("Доступ разрешен")
else:
    print("Неверный логин или пароль")
