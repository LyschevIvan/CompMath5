import matplotlib.pyplot as plt
import numpy as np
import math

X = []
Y = []


def equation():
    X = []
    Y = []
    print("\nВыберите уравнение:\n"
          "1. sin(x)\n"
          "2. sqrt(x)\n"
          "3. 3*x^2 + x/2 + 1\n"
          "4. e^x\n")
    method = int(input())
    print("\nВыберите границу (через пробел):")
    borders = list(input().split(" "))
    a = float(borders[0].strip())
    b = float(borders[1].strip())
    print("\nКоличество точек интерполирования: ")
    number_of_data = int(input())
    x = np.linspace(a, b, number_of_data)

    if method == 1:
        for i in range(number_of_data):
            X += [x[i]]
            Y += [math.sin(x[i])]
    elif method == 2:
        for i in range(number_of_data):
            X += [x[i]]
            Y += [math.sqrt(x[i])]
    elif method == 3:
        for i in range(number_of_data):
            X += [x[i]]
            Y += [3 * math.pow(x[i], 2) + 0.5 * x[i] + 1]
    elif method == 4:
        for i in range(number_of_data):
            X += [x[i]]
            Y += [math.pow(math.e, x[i])]
    return X, Y


def lagrange(x):
    res = 0
    l_n = []
    for j in range(len(Y)):
        c = 1
        for i in range(len(X)):
            if i != j:
                c *= (x - X[i]) / (X[j] - X[i])
        l_n.append(Y[j] * c)
        res += Y[j] * c
    return res


def check_dist(X):
    h = X[1] - X[0]
    for i in range(len(X) - 1):
        if X[i + 1] - X[i] != h:
            return False
    return True


def calc_diff(arr):
    res = []
    for i in range(len(arr) - 1):
        res += [arr[i + 1] - arr[i]]
    return res


def newton(x):
    dy_n = [Y]
    h = X[1] - X[0]
    tmp = Y
    for i in range(len(Y) - 1):
        tmp = calc_diff(tmp)
        dy_n += [tmp]

    left = 0
    for i in range(len(X) - 1):
        if X[i] <= x < X[i + 1]:
            left = i
            break
    if x == X[-1]:
        left = len(X)-1

    if x - X[0] <= X[-1] - x:
        t = (x - X[left]) / h
        summ = Y[left]
        for i in range(1, len(X) - left - 1):
            summ += t * dy_n[i][left] / math.factorial(i)
            t *= (t - i)

    else:

        if left == len(X) - 1:
            right = left
        else:
            right = left + 1

        t = (x - X[right]) / h
        summ = Y[right]
        for i in range(1, right):
            summ += t * dy_n[i][right - i] / math.factorial(i)
            t *= (i + t)
    return summ


def print_graph(func, dot):
    fig, ax = plt.subplots()
    x = np.linspace(np.min(X), np.max(X), 100)
    y = [func(x) for x in x]
    plt.plot(X, Y, 'o', color='r', label='input data')
    plt.plot(x, y, color='b', label='approximate function')
    plt.plot(dot[0], dot[1], '+', color='g', markersize=12, label='answer')

    ax.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    X = []
    Y = []

    print("Выберите тип ввода")
    print("1 - из файла")
    print("2 - выбор из функций")
    c = int(input())
    if c == 1:
        with open('input.txt', 'r') as file:
            for line in file:

                X += [int(line.split()[0])]
                Y += [int(line.split()[1])]
    elif c == 2:
        X, Y = equation()
        print(X)
        print(Y)


    print("Выберите метод интерполирования")
    print("1 – Метод Лагранжа")
    print("2 – Метод Ньютона c конечными разностями")

    c = int(input())
    print("Введие х для интерполирования")
    print("{} <= x <= {}".format(min(X), max(X)))
    x = float(input())
    if min(X) <= x <= max(X):

        if c == 1:

            res = lagrange(x)
            print_graph(lagrange, [x, res])
            print(res)

        elif c == 2:
            if check_dist(X):
                res = newton(x)
                print_graph(newton, [x, res])

                print(res)
            else:
                print("Узлы не равноудалены!")
    else:
        print("Промежуток неверен")
