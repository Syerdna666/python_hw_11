# Задача 1. Постройте график функции
# 𝑓 𝑥 = 5𝑥^2 + 10𝑥 − 30
# По графику определите, при каких значения x значение функции отрицательно.

from sympy import *
from random import randint as RI
from matplotlib import pyplot as plt


def Task1():
    x = symbols('x')
    func = 5*x*x + 10*x - 30

    negative_x = solve(func)
    print(f'значения функции отрицательны на отрезке: {negative_x}')

    plot(func)

Task1()

# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость 
# квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома
# и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. 
# Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.



area_houses = [RI(100, 300) for i in range(15)]
print(f'Площади домов: {area_houses}')

prices_houses = [RI(3, 20) for i in range(15)]
print(f'Цены домов: {prices_houses}')


fig,ax = plt.subplots()
ax.bar(area_houses, prices_houses)
plt.title("Зависимость цены дома от его площади")
plt.ylabel("Цена в млн")
plt.xlabel("Площадь в кв. метрах")
plt.show()

houses_mean = []
for i in range(15):
    houses_mean.append(prices_houses[i]/area_houses[i] * 1000)
print(f'Средняя цена за кв.м в тыс. руб: {houses_mean}')

plt.bar(list(range(1,16)), houses_mean)
plt.title("Средняя цена за кв.м в тыс. руб")
plt.ylabel("Цена в тыс. руб")
plt.xlabel("номер дома")
plt.show()



houses = list(zip(area_houses, prices_houses, houses_mean))
houses = list(filter(lambda x: x[2]<50, houses))
result = sorted(houses, key=lambda x: x[0])
print(result)
print(f'список домов (площадь, цена, цена за кв.м): {result}')
