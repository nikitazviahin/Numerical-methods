import numpy
import matplotlib.pyplot as plt

xdigits = [0,1,2,3,4,5]
ydigits = [3.8,10.4,19.6,34.6,51.4,75]

print("массив точок x:")
for i in xdigits:
    print(xdigits[i], end=' ')

print("\n")

print("массив точок y:")
for i in range(len(ydigits)):
    print(ydigits[i], end='  ')

a = 0
b = 0

print("\n\nвиберіть апроксимуючу функцію (1 для лінійної, 2 для квадратичної): ",end ="")
typ = int(input())

if (typ == 1):

    print("\n\nвиберіть порядок округлення: ",end ="")
    n = int(input())

    b00 = 0
    for i in xdigits:
        b00 = (xdigits[i]**2) + b00

    b01 = 0
    for i in xdigits:
        b01 = xdigits[i] + b01

    b11 = len(xdigits)

    c0 = 0
    for i in xdigits:
        c0 = c0 + (xdigits[i]*ydigits[i])

    c1 = 0
    for i in range(len(ydigits)):
        c1 = c1 + ydigits[i]

    a = (c0*b11-b01*c1)/(b11*b00-b01**2)
    b = (c1-b01*a)/(b11)



    if (b >= 0) :
        print("\n\nвигляд лінійної апроксимуючої функції: ", round(a,n),"x +",round(b,n))
    else:
        print("\n\nвигляд лінійної апроксимуючої функції: ", round(a,n),"x ",round(b,n))

    print("\n\nпрогноз для точки x = 6: ", "(","6",";",round(a*6 + b,n),")")

    delta = []
    for i in xdigits:
        d = abs(((a*xdigits[i] + b) - ydigits[i])/ydigits[i])
        delta.append(d)

    print("\nпохибка обчислення становить ", max(delta))

    fig, ax = plt.subplots()
    x = numpy.linspace(-5,8,200)
    y = a*x + b
    ax.plot(x,y)
    for i in xdigits:
        x = xdigits[i]
        y = ydigits[i]
        plt.scatter(x,y)
    plt.show()
    
else:
    
    print("\n\nвиберіть порядок округлення: ",end ="")
    n = int(input())

    b00 = 0
    for i in xdigits:
        b00 = (xdigits[i]**4) + b00

    b01 = 0
    for i in xdigits:
        b01 = (xdigits[i]**3) + b01

    b02 = 0
    for i in xdigits:
        b02 = (xdigits[i]**2) + b02

    b12 = 0
    for i in xdigits:
        b12 = xdigits[i] + b12

    b11 = 0
    for i in xdigits:
        b11 = (xdigits[i]**2) + b11

    b22 = len(xdigits)

    c0 = 0
    for i in xdigits:
        c0 = c0 + ydigits[i]*(xdigits[i]**2)

    c1 = 0
    for i in xdigits:
        c1 = c1 + ydigits[i]*xdigits[i]

    c2 = 0
    for i in range(len(ydigits)):
        c2 = c2 + ydigits[i]

    M1 = numpy.array([[b00, b01, b02],[b01, b11, b12],[b02, b12, b22]])
    v1 = numpy.array([c0, c1, c2])
    w = numpy.linalg.solve(M1, v1)

    print("вигляд квадратичної апроксимуючої функції: ", round(w[0],n), "x**2 +", round(w[1],n), "x +", round(w[2],n))

    print("\n\nпрогноз для точки x = 6: ", "(","6",";",round(w[0]*36 + w[1]*6 + w[2],n),")")

    delta = []
    for i in xdigits:
        d = abs(((w[0]*(xdigits[i]**2) + w[1]*xdigits[i] + w[2]) - ydigits[i])/ydigits[i])
        delta.append(d)

    print("\nпохибка обчислення становить ", max(delta))

    fig, ax = plt.subplots()
    x = numpy.linspace(-5,8,200)
    y = w[0]*(x**2)+w[1]*x+w[2]
    ax.plot(x,y)
    for i in xdigits:
        x = xdigits[i]
        y = ydigits[i]
        plt.scatter(x,y)
    plt.show()
    
    




