# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# Пусть 1 - лежит решкой, 0 - гербом

# N = int(input("Введите кол-во монеток на столе: "))
# heads_amount = 0
# tails_amount = 0
# i = 1
# while i <= N:
#     coin = int(input(f'Введите значение для {i}-ой монеты: '))
#     if coin == 1:
#         heads_amount += 1
#     else:
#         tails_amount += 1
#     i += 1
# if heads_amount < tails_amount:
#     print(heads_amount)
# else:
#     print(tails_amount)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# sum_digit = int(input('Введите сумму чисел: '))
# pow_digit = int(input('Введите произведение чисел: '))
# discrim = sum_digit**2 - 4 * pow_digit
# digit_1 = int((sum_digit + discrim ** 0.5) / 2)
# digit_2 = int((sum_digit - discrim ** 0.5) / 2)
# print(f'Загаданное число: {digit_1}{digit_2}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input('Введите число N: '))
# k = 0
# while 2**k <= N:
#     print(f'k = {k}, 2**k = {2**k} ')
#     k += 1