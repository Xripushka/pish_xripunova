#1задача
n = int(input("Введите натуральное число (не более 100): "))  
  
# Проверка корректности ввода  
if n > 100 or n < 1:  
    print("должно быть натуральным и не превышать 100")  
else:  
    # Вывод квадратов и кубов  
    for i in range(1, n + 1):  
        print(i**2, i**3)  

#2задача
a = int(input("Введите число a (от 0 до 100): "))  
b = int(input("Введите число b (от 0 до 100): "))  
  
if a > b:  
    print("Ошибка: a должно быть меньше или равно b")  
else:  
    for number in range(a, b + 1):  
        square = number ** 2  
        print(square)

#3задача
c = int(input("Введите число c (от 0 до 100): "))  
d = int(input("Введите число d (от 0 до 100): "))  
  
if c > d:  
    print("Ошибка: c должно быть меньше или равно d")  
else:  
    sum_squares = sum(i**2 for i in range(c, d+1))  
    print(sum_squares)

#4задача
number = input("Введите число (неоднозначное): ")  
  
is_ascending = True  
for e in range(len(number) - 1):  
    if number[e] >= number[e + 1]:  
        is_ascending = False  
        break  
  
# Выводим результат  
if is_ascending:  
    print("Да, цифры расположены в порядке возрастания")  
else:  
    print("Нет, цифры не расположены в порядке возрастания")