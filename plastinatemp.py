import math                         #Звягин Н.С. КМ-73 Вариант №5, был выбран метод сеток

def get_matrix(top,bot,left,right): #функция, которая подготовит матрицу начальных значений, которые мы знаем ( граничные)
    matrix = []                     #а значения, не являющиеся граничными, положим равными начальному приближению,
    for i in range(7):              #которое в методе сеток выбирается, как среднее арифмитическое граничных значений в каждой точке
        matrix.append([])
    for i in range(7):
        matrix[i].append(left)
    for i in range(1,5):
        matrix[0].append(top)
        for j in range(1,6):
            average = (top+bot+left+right)/4
            matrix[j].append(average)
        matrix[6].append(bot)
    for i in range(7):
        matrix[i].append(right)
    return matrix;

def compute_temperature(dx,dy,matrix): #основная функция, которая использует метод простых итераций, метод сеток
    for k in range(100):               #и формулу  Uij= (dy^2(Ui+1,j + Ui-1,j) + dx^2(Ui,j+1 + Ui,j-1))/2*(dx^2+dy^2)
        for i in range(1,6):
            for j in range(1,5):
                matrix[i][j] = round((((pow(dx,2)*(matrix[i][j-1]+matrix[i][j+1])) +
                                (pow(dy,2)*(matrix[i-1][j]+matrix[i+1][j])))/(2*(pow(dx,2)+pow(dy,2)))),2)
    return matrix;



while(True):
    toptemp = int(input("Введіть температуру верхньої межі: ")) #блок для ввода данных, в моём варианте №5
    bottemp = int(input("Введіть температуру нижньої межі: "))  #toptemp = 400, bottemp = 1050, lefttemp = 280
    lefttemp = int(input("Введіть температуру лівої межі: "))   #righttemp = 370, deltax = 3.77, deltay = 2.22
    righttemp = int(input("Введіть температуру правої межі: "))
    deltax = float(input("Введіть проміжок по вертикалі: "))
    deltay = float(input("Введіть проміжок по горизонталі: "))
    partly_matrix = get_matrix(toptemp,bottemp,lefttemp,righttemp)
    
    result = compute_temperature(deltax,deltay,partly_matrix)
    print("Розподіл температури на пластині у вигляді матриці: ")
    for i in range(7):
        print(result[i])
    answer = input("Ще раз? (y/n)")
    if answer == 'y':
        continue
    else:
        break
    


