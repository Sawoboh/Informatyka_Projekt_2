# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

K=[[1,1],[4,2],[3,2],[4,3],[2,4],[2.5,2.5]]



if len(K) > 2:
    suma=0
    for i in range(len(K)):
        if i<len(K)-1:
            P=(K[i][0]*(K[i+1][1]-K[i-1][1]))
            print(P)
            suma += P
    P=(K[-1][0]*(K[0][1]-K[-2][1]))
    suma += P
    suma=0.5*suma    
    print(suma)