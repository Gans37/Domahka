# 3.Напишите программу, которая принимает 
# на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
#  номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))


if x == 0 and y == 0:
    print('Вы не услышали условия поэтому Вы находитесь в начале начал ;)')
elif x > 0 and y > 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
elif x < 0 and y > 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
elif x < 0 and y < 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
elif x > 0 and y < 0:
    print(
        f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')