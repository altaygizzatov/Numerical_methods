import matplotlib.pyplot as plt
import numpy as np


nX = 10
xA = 0
xB = 10
#dX = (xB - xA)/(nX - 1)

nT = 60
tA = 0
tB = 10

def f0(x):
    if x <= 5:
        return 0
    elif x <= 10:
        return 1

def resh():

    x = np.linspace(xA, xB, nX)
    dX = x[1] - x[0]

    t = np.linspace(tA, tB, nT)
    dT = t[1] - t[0]

    SdTM = np.array([np.zeros(nX) for i in range(nX)])
    SdTM[0][0] = 0.5

    for i in range(1, nX-1):
        SdTM[i][i-1] = dX/6 + dT/dX
        SdTM[i][i] = 2*dX/3 - 2*dT/dX
        SdTM[i][i+1] = dX/6 + dT/dX

    #for i in range (0, nX-1):
        #SdTM[i][0] = 0.5
    SdTM[nX-1][nX -1] = 1
    #print(SdTM)
    S = np.array([np.zeros(nX) for i in range(nX)])

    for i in range(1, nX-1, 1):
        S[i][i-1] = dX/6
        S[i][i] = 2*dX/3
        S[i][i+1] = dX/6

    S[0][0] = 1
    S[0][1] = - 1
    S[nX-1][nX -1] = 1
    u = np.array([[f0(i) for i in x]])

    for i in range(0, nT-1, 1):
        tmp = np.dot(SdTM, u[i])
        u = np.append(u, [np.linalg.solve(S, tmp)], axis=0)

    for i in range(0, nT, int(nT/5)):
        plt.plot(x, u[i])
    
    #plt.plot(x,u[nT-1])
    plt.show()

resh()
