# numbers = 1, 2, 3, 4
#
# for i in numbers:
#     print(i)
#
#
# for i in range(1, 10, -1):
#     print(1)


# ww = int(input("Введите нижнюю границу диапазона:"))
# www = int(input("Введите верхнюю границу диапазона:"))
# for i in range(www, ww, -1):
#     if i % 5 == 0:
#         if i % 10 == 0:
#             continue
#         print(i)

# for letter in 'стоп':
#     if letter == 'т':
#         continue
#     print(letter)

# ww = int(input("Введите нижнюю границу диапазона:"))
# www = int(input("Введите верхнюю границу диапазона:"))
# for i in range(www, ww, -1):
#     if i % 2 == 0:
#         if i % 5 == 0:
#             continue
#         print(i)

# start = int(input('введите начало последовательности: '))
# stop = int(input('введите конец последовательности: '))
#
# otr = 0
# pol = 0
#
# for number in range(start, stop):
#     if number < 0:
#         otr += number
#     else:
#         pol += number
#
# print(f'сумма положительных чисел: {pol}')
# print(f'сумма отрицательных чисел: {otr}')
#
# start = int(input('введите начало последовательности: '))
# stop = int(input('введите конец последовательности: '))
#
# quantity = 0
# sum_of_numbers = 0
#
# for number in range(start, stop):
#     sum_of_numbers += number
#     quantity += 1
#
# final = sum_of_numbers // quantity
#
# print(f'среднее арифметическое последовательности от {start} до {stop}: {final}')

# number_of_string = 1
#
# for i in range(1, 6):
#     print(f'строка {number_of_string} 0')
#     number_of_string += 1

# n = int(input('введите число: '))
#
# for i in range(1, n+1):
#     if n > 7:
#         break
#     if i == 1:
#         print('красный')
#     if i == 2:
#         print('оранжевый')
#     if i == 3:
#         print('желтый')
#     if i == 4:
#         print('зеленый')
#     if i == 5:
#         print('голубой')
#     if i == 6:
#         print('синий')
#     if i == 7:
#         print('фиолетовый')
#
# if n > 7 or n < 1:
#     print('радуга состоит из семи цветов')
# n = int(input('аоаоаоао'))
#
# print(f'{n} x 1 = {n * 1}')
# print(f'{n} x 2 = {n * 2}')
# print(f'{n} x 3 = {n * 3}')
# print(f'{n} x 4 = {n * 4}')
# print(f'{n} x 5 = {n * 5}')
# print(f'{n} x 6 = {n * 6}')
# print(f'{n} x 7 = {n * 7}')
# print(f'{n} x 8 = {n * 8}')
# print(f'{n} x 9 = {n * 9}')
# print(f'{n} x 10 = {n * 10}')
#
# for i in range(1, 11):
#     print(f'{n} x {i} = {n * i}')
