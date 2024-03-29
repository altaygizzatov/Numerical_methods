import matplotlib.pyplot as plt
import numpy as np

nX = 100
xA = 0
xB = 6
pi = 3.14

def F1(dX, x):
    return -dX**2/2 * x * np.sin(np.pi * x)

def F2(dX, x):
    return -dX ** 2 / 2 * x * np.cos(np.pi * x)
def resh():
    x = np.linspace(xA, xB, nX)
    dX = x[1] - x[0]
    #print(dX)

    A = 1
    B = (3.0/2.0*dX - 2.0)
    C = (1.0 - 3.0/2.0*dX)

    diagMatrix = np.array([np.zeros(nX) for i in range(nX)])
    diagMatrix[0][0] = 1
    diagMatrix[0][1] = -1

    for i in range(1, nX - 1):
        diagMatrix[i][i-1] = C
        diagMatrix[i][i] = B
        diagMatrix[i][i+1] = A
    diagMatrix[nX-1][nX-1] = 1

    f = np.array([F1(dX, i) for i in x])
    f[0] = 0
    f[nX-1] = 2
    u = np.linalg.solve(diagMatrix, f)

    plt.title('Phi(x)')
    plt.xlabel('x')
    plt.ylabel('Phi')
    plt.plot(x, u)
    #plt.plot(2*x*np.cos(pi*x)/(9+4*pi**2)-9*(3+4*pi**2)*np.cos(pi*x)/(pi**2*(4*pi**2+9)**2)-3*x*np.sin(pi*x)/(pi*(9+4*pi**2))-16*pi*np.sin(pi*x)/(4*pi**2+9)**2-np.exp(-3/2*x)+1.73)
    plt.show()

resh()

