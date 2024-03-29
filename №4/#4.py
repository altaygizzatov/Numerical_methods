import matplotlib.pyplot as plt
import numpy as np

nX = 1000
xA = 0
xB = 1

ro = 1
ksi = 0.1
v = 2.5

def fAlalitic(x):
    return - (np.exp(ro * v * xB / ksi)) / (- np.exp(ro * v * xB / ksi) + 1) + (np.exp(ro * v * x / ksi)) / (-np.exp(ro * v * xB / ksi) + 1)

def resh():
    x = np.linspace(xA, xB, nX)
    dX = x[1] - x[0]

    A = -1 - ro * v * dX / ksi
    B = 2 + ro * v * dX / ksi
    C = -1
    #print(A, B, C)

    diagMatrix = np.array([np.zeros(nX) for i in range(nX)])
    diagMatrix[0][0] = 1

    for i in range(1, nX - 1):
        diagMatrix[i][i-1] = A
        diagMatrix[i][i] = B
        diagMatrix[i][i+1] = C

    diagMatrix[nX-1][nX-1] = 1
    #print(diagMatrix)
    f = np.zeros(nX)
    f[0] = 1

    u = np.linalg.solve(diagMatrix, f)
    plt.plot(x, u, 'o', label='Numerical')
    plt.legend()

    f_A = np.array([fAlalitic(i) for i in x])
    plt.plot(x, f_A, label='Theoretical')
    plt.legend()

    plt.show()


resh()

