import numpy as np
import matplotlib.pyplot as plt


nX = 100
xA = 0
xB = 8.0
dX = (xB - xA)/nX

def analit(x):
    return x**4/4-2*x

def resh():
    x = np.linspace(xA, xB, nX)

    diagMatrix = np.array([np.zeros(nX) for i in range(nX)])

    for i in range(1, nX - 1):
        diagMatrix[i][i - 1] = 1/(x[i]-x[i-1])
        diagMatrix[i][i] = -1 / (x[i] - x[i - 1]) - 1/(x[i+1]-x[i])
        diagMatrix[i][i + 1] = 1 / (x[i+1] - x[i])

    diagMatrix[0][0] = 1
    diagMatrix[nX-1][nX-2] = -1
    diagMatrix[nX - 1][nX - 1] = 1

    f = np.zeros(nX)

    for i in range(1, nX - 1):
        f[i] = 3*((x[i])**4-(x[i-1])**4)/(4*(x[i]-x[i-1])) - x[i-1]*((x[i])**3-(x[i-1])**3)/(x[i]-x[i-1]) + x[i+1]*((x[i+1])**3-(x[i])**3)/(x[i+1]-x[i]) - 3*((x[i+1])**4-(x[i])**4)/(4*(x[i+1]-x[i]))

    f[0] = 0
    f[nX-1] = 510 * dX

    u = np.linalg.solve(diagMatrix, f)
    plt.plot(x, u, label='numerical')

    plt.plot(x,analit(x), label='theoretical')

    plt.xlabel('x')
    plt.ylabel('Phi')
    plt.legend()
    plt.show()

resh()