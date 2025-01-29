# Преобразование типов данных в Python


num_str = "10"
num_int = int(num_str)  # 10 (целое число)
num_float = float(num_str)  # 10.0 (число с плавающей точкой)

print(num_int, type(num_int))  # 10 <class 'int'>
print(num_float, type(num_float))  # 10.0 <class 'float'>


num = 42
num_str = str(num)  # '42'
print(num_str, type(num_str))  # '42' <class 'str'>


print(bool(""))  # False (пустая строка = ложь)
print(bool("Hello"))  # True (непустая строка = истина)
