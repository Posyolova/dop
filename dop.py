import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
x_start = float(input("Введите значение X начальная: "))
x_end = float(input("Введите значение X конечная: "))
dx = float(input("Введите значение dX: "))
#запрашиваем значения a, b, c, X начальная, X конечная и dX с помощью функции input и преобразуем их в тип float.

def F(a, b, c, x):
    if a < 0 and x != 0:
        return a*x**2 + b**2*x
    elif a > 0 and x == 0:
        return math.floor(a) + math.floor(b) + math.floor(c)#если выполняет условие то возвращает сумму округленных значений
    else:
        ac = int(abs(a))
        bc = int(abs(b))
        cc = int(abs(c))#производятся операции с абсолютными значениями
        not_ac = ~ac
        and_bc_cc = bc & cc
        or_and = and_bc_cc | not_ac
        or_vc = or_and | cc #побитовые операции
        if or_vc != 0 and (or_and != 0 or cc != 0):
            return a*x**2 + b**2*x
        else:
            return math.floor(a*x + b/x - c + 1)#возвращается результат выражения 

print("  x      |      F(x) ")
print("--------------------")
x = x_start
while x <= x_end:
    fx = F(a, b, c, x)
    print("{:.4f}   |   {:.4f}".format(x, fx))
    x += dx
#выводим заголовок таблицы и начинаем цикл, который будет выводить значения функции F для каждого значения x в заданном диапазоне с шагом dX.

fx = F(a, b, c, x)
print("{:.4f}   |   {:.4f}".format(x, fx))
#вызываем функцию F с текущим значением x и сохраняем результат в переменную fx. Затем мы выводим значения x и fx в таблицу с помощью функции print и форматирования строк.

x += dx
# конец программы
