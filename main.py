#Задача 2

x = input('Введите трехзначный Х: ')

if (int(x) > 1000) or (int(x) < 100) :
    print('Х только трехзначный положительный!')
else:
    print('Сумма цифр введенного числа = ' + str(int(x[0])+int(x[1])+int(x[2])))

#Задача 4
flu = input('Введите общее количество журавликов (кратное 6): ')
if (int(flu) % 6 ==0):
    flu = int(flu)
    print('Петя ' + str(round(flu/6)) + ' шт')
    print('Сережа ' + str(round(flu/6)) + ' шт')
    print('Катя ' + str(round((flu/6)*4)) + ' шт')
else:
    print('Некорректные данные!')

#Задача 6
num = input('Введите шестизначный номер билета: ')

if len(num) == 6:
    if ((int(num[0]) + int(num[1]) + int(num[2])) == (int(num[3]) + int(num[4]) + int(num[5]))):
        print('Счастливый билет')
    else:
        print('Обыкновенный билет')
else:
    print('Ошибка, билет должен быть шестизначный')



#Задача 8

n = input('Введите n: ')
m = input('Введите m: ')
k = input('Введите k: ')
n = int(n)
m = int(m)
k = int(k)


if (not(k % m) or not(k % n)) and (k < m * n):
    print('Можно разделить')
else:
    print('Нельзя разделить')
