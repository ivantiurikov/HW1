#Задача 2: Найдите сумму цифр трехзначного числа.
# number = int(input('Введите трехзначное число: '))
# digit_1 = number // 100
# digit_2 = number // 10 % 10
# digit_3 = number % 10
# print(digit_1 + digit_2 + digit_3)

#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# amount = int(input('Введите количество журавликов: '))
# amount_boy = amount / 6
# amount_girl = amount_boy * 4
# print(amount_boy, amount_girl, amount_boy)

#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.

# ticket = int(input('Введите номер билета: '))
# half_1 = ticket // 1000
# half_2 = ticket % 1000
# sum_half_1 = half_1 // 100 + half_1 // 10 % 10 + half_1 % 10
# sum_half_2 = half_2 // 100 + half_2 // 10 % 10 + half_2 % 10
# if sum_half_1 == sum_half_2:
#     print('YES')
# else:
#     print('NO')

#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите ширину плитки: '))
# m = int(input('Введите длину плитки: '))
# k = int(input('Введите количество долек: '))
# if k == n or k == m or ((k % n == 0 and k / n < m) or (k % m == 0 and k / m < n)):
#     print('YES')
# else:
#     print('NO')