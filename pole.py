# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

K=[[1,1],[1,2],[2,2],[2,1]]



if len(K) > 2:
    suma=0
    for i in range(len(K)):
        if i<len(K)-1:
            P=(K[i][0]*(K[i+1][1]-K[i-1][1]))
            suma += P
    P=(K[-1][0]*(K[0][1]-K[-2][1]))
    suma += P
    suma=0.5*abs(suma)    
    print(suma)

X = []
Y = []
for i in range(len(K)):
    X.append(K[i][0])
    Y.append(K[i][1])
n = len(K)
pole = 0
for i in range(n-1):
    x1 = X[i]
    y1 = Y[i]
    x2 = X[i+1]
    y2 = Y[i+1]
    pole += x1 * y2 - x2 * y1
    
pole /= 2
pole_m2 = abs(pole)
poletxt = f"Pole: {pole_m2:.3f} [m2]"
print(poletxt)
    