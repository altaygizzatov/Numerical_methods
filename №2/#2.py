import numpy as np
import matplotlib.pyplot as plt

D = 1 # коэффициент диффузии

nX = 10 # число шагов по x
xA = 0 # значение x на левой границе
xB= 10 # значение x на правой границе
dX = xB/nX # шаг по x

T = 10 # максимальное значение времени t на правой границе
nT = 100 # число шагов по t
dT = T / nT # шаг по t

# Начальные условия
def f0(x):
    if (x <= 5) and (x >= 0):
        return 0
    elif (x > 5) and (x <= 10):
        return 5

# Явная схема
def Yavnoe():
    x_i = np.arange(0, xB, dX)  # значения в узлах по х
    t_j = np.arange(0, T, dT)  # значение в узлах по t
    r_j = len(t_j)  # количество узлов по t
    r_i = len(x_i)  # количество узлов по x

    w_h_t = np.zeros([r_j, r_i])  # итоговая сетка размером x_i*t_j

    # граничные условия
    for j in range(r_j):
        w_h_t[j, 0] = 0
        w_h_t[j, r_i - 1] = 5

    # начальное условие, заполнение нулвого слоя
    for i in range(r_i):
        w_h_t[0, i] = f0(x_i[i])

    const = D * dT / (dX ** 2)
    for i in range(len(w_h_t) - 1):
        for j in range(1, len(x_i) - 1):
            w_h_t[i + 1, j] = w_h_t[i, j] + const * (w_h_t[i, j + 1] - 2 * w_h_t[i, j] + w_h_t[i, j - 1])

    plot_ = np.arange(0, len(w_h_t) - 1, 1)
    for y in range(0, len(w_h_t)):
        plt.plot(x_i, w_h_t[y])

    plt.title('Yavnoe')
    plt.show()


# Неявная схема
def neYavnoe():
    X = [xA + dX * i for i in range(nX)]
    A = (1 + 2*D/(dX*dX) * dT)
    B = -D/(dX*dX) * dT
    C = -D/(dX*dX) * dT

    matrix = np.array([[f0(x) for x in X]])
    diagMatrix = np.array([np.zeros(nX) for i in range(nX)])
    diagMatrix[0][0] = 1

    for i in range(1, nX - 1):
        diagMatrix[i][i-1] = C
        diagMatrix[i][i] = A
        diagMatrix[i][i+1] = B
    diagMatrix[nX-1][nX-1] = 1

    for i in range(nT - 1):
        matrix = np.append(matrix, [np.linalg.solve(diagMatrix, matrix[i])], axis=0)

    for i in range(0, len(matrix), int(len(matrix)/10)):
        plt.plot(X, matrix[i])

    plt.title('neYavnoe')
    plt.xlabel("x")
    plt.ylabel("Ф(x)")
    plt.show()




Yavnoe()
neYavnoe()
