import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg
import seaborn as sns


def spline(x, y, sno, sn1, sn2, sn3): #Підрахунок сплайну
    newx = []
    newy = [[], [], []]
    for i in range(len(sno)):
        xs = np.arange(x[i], x[i+1] + 0.1, 0.1)
        newx.append(xs)
        for j in range(len(xs)):
            res = sno[i] + sn1[i] *(xs[j] - x[i]) + \
                  sn2[i] *(xs[j] - x[i]) ** 2 + sn3[i] * (xs[j] - x[i]) ** 3
            newy[i].append(res)

    sns.set()
    plt.plot(x, y, 'o', label='data')
    plt.plot(newx[0], newy[0], label='S0')
    plt.plot(newx[1], newy[1], label='S1')
    plt.plot(newx[2], newy[2], label='S2')
    plt.xlim(-4, 7)
    plt.legend(loc='upper left', ncol=2)
    plt.show()
    

def find_ms(hs, ds, s1, s2):   #Розв'язок системи
    ms = []
    row1 = [((3 / 2) * hs[0] + 2 * hs[1]), hs[1]]
    row2 = [hs[1], 2 * hs[1] + (3 / 2) * hs[2]]

    nmat = np.array([row1, row2])
    cons = np.array([6 * (ds[1] - ds[0]) - 3 * (ds[0] - s1),
                     6 * (ds[2] - ds[1]) - 3 * (s2 - ds[2])])

    answer = linalg.solve(nmat, cons)
    for i in range(len(answer)):
        res = answer[i]
        ms.append(res)
        
    ms.append((3 / hs[2]) * (s2 - ds[2]) - (answer[1] / 2))
    ms.insert(0, (3 / hs[2]) * (ds[0] - s1) - (answer[0] / 2))
    return ms


def find_ss(ms, hs, ds):
    sn1, sn2, sn3 = [], [], []
    
    for i in range(len(ms) - 1):
         res = ds[i] - (hs[i] / 6) * (2 * ms[i] + ms[i+1])
         sn1.append(res)

    for i in range(len(ms) - 1):
        sn2.append(ms[i] / 2)

    for i in range(len(ms) - 1):
        res = (ms[i+1] - ms[i]) / (6 * hs[i])
        sn3.append(res)
        
    
    return sn1, sn2, sn3
    

def calc_polinoms(x, y, s1, s2): #Знаходження коефіцієнтів d i h
    sno = [y[0], y[1], y[2]]     #Формули d = (yk+1-yk)/hk
    hs = []                      #h = xk+1-xk
    ds = []

    for i in range(len(x) - 1):
        res = x[i+1] - x[i]
        hs.append(res)

    for i in range(len(y) - 1):
        res = (y[i+1] - y[i]) / hs[i]
        ds.append(res)

    ms = find_ms(hs, ds, s1, s2)
    sn1, sn2, sn3= find_ss(ms, hs, ds)

    for i in range(len(sno)):
        print('\n S{} = {} + ({})(x - {}) + ({})(x - {})^2 + ({})(x - {})^3'.format(i, round(sno[i],3), round(sn1[i],3),
                                                                              x[i], round(sn2[i], 3), x[i],
                                                                              round(sn3[i], 3), x[i]))
    return sno, sn1, sn2, sn3
    

if __name__ == "__main__":
    print('Лаб.раб. #2 \n Звягін Микита КМ-73 Варіант 5')
    while(True):
        x = [-4, 1, 3, 7]
        y = [2, 5, -3, 0]
        s1 = -1
        s2 = 2
        sno, sn1, sn2, sn3 = calc_polinoms(x,y, s1, s2)
        
        spline(x, y, sno, sn1, sn2, sn3)
        
        ans = input('Обчислити x?(y/n)')
        if ans == 'y':
            xo = float(input('Введіть x для обчислення значення функції:'))
            if xo >= -4 and xo <= 1:
                yo = sno[0] + sn1[0] *(xo - x[0]) + \
                     sn2[0] *(xo - x[0]) ** 2 + sn3[0] *(xo - x[0]) ** 3
                print('Y =', yo)
            elif xo >= 1 and xo <= 3:
                yo = sno[1] + sn1[1] *(xo - x[1]) + \
                     sn2[1] *(xo - x[1]) ** 2 + sn3[1] *(xo - x[1]) ** 3
                print('Y =', yo)
            elif xo >= 3 and xo <= 7:
                yo = sno[2] + sn1[2] *(xo - x[2]) + \
                     sn2[2] *(xo - x[2]) ** 2 + sn3[2] *(xo - x[2]) ** 3
                print('Y =', yo)
            else:
                print('X за межами області визначень функції!')
        else:
            answer = input('Повторити?(y/n):')
            if answer == 'y':
                continue
            else:
                break
            
        answer = input('Повторити?(y/n):')
        if answer == 'y':
            continue
        else:
            break
