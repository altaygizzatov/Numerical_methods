import matplotlib.pyplot as plt
import numpy as np

nX = 100 # Количество разбиений
xA = 0 # Левая граница
xB = 10 # Правая граница
dX = (xB - xA) / (nX - 1) # Шаг по x

nT = 100
tA = 0
tB = 0.5
dT = (tB - tA) / (nT - 1)

V = 2.5

# Начальное условие
def f0(x):
    if (x < 4) and (x >= 0):
        return 0
    elif (x >= 4) and (x <= 10):
        return 1

# Явная схема
def Yavnoe():
    matrix = []
    X = [xA + dX * i for i in range(nX)]
    f_0 = []

    for i in range(nX):
        f_0.append(f0(i * dX))
    matrix.append(f_0)


    for i in range(nT - 1):
        f_tmp = []
        f_tmp.append(0)
        for j in range(1, nX):
            f_tmp.append(matrix[i][j] - V * dT / (dX) * (matrix[i][j] - matrix[i][j - 1]))
        matrix.append(f_tmp)

    plt.title('Yavnoe')
    plt.xlabel("x")
    plt.ylabel("Ф(x)")
    plt.plot(X, matrix[0])


    for i in range(0, len(matrix), int(len(matrix) / 10)):
        plt.plot(X, matrix[i])

    plt.show()


# Неявная схема
def neYavnoe():
    X = [xA + dX * i for i in range(nX)]
    A = (1 + V/(dX) * dT)
    B = -V/(dX) * dT
    matrix = np.array([[f0(x) for x in X]])
    diagMatrix = np.array([np.zeros(nX) for _ in range(nX)])
    diagMatrix[0][0] = 1

    for i in range(1, nX):
        diagMatrix[i][i-1] = B
        diagMatrix[i][i] = A

    for i in range(nT - 1):
        matrix = np.append(matrix, [np.linalg.solve(diagMatrix, matrix[i])], axis=0)

    for i in range(0, len(matrix), int(len(matrix)/10)):
        plt.plot(X, matrix[i])

    plt.title('Neyavnoe')
    plt.xlabel("x")
    plt.ylabel("Ф(x)")
    plt.show()


# Условие сходимости
if V*dT/dX<= 1.0:
    Yavnoe()
    neYavnoe()

else: print('Error')


