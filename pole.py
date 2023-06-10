# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:16:52 2023

@author: amaks
"""

'''pole powierzchni'''

'''K=[[521912.62,610971.36],[521918.62,610973.36],[521915.62,610977.36]]'''
K=[[1,1],[3,3],[6,7],[4,4],[2,4]]
pole=0
for i in range(len(K)):
    x1=K[i][0]
    y1=K[i][1]
    x2=K[(i+1) % len(K)][0]
    y2=K[(i+1) % len(K)][1] 
    pole += x1*y2 - x2*y1
print(abs(pole/2))



suma=0
for i in range(len(K)):
    if i<len(K)-1:
        P=(K[i][0]*(K[i+1][1]-K[i-1][1]))
        suma += P
P=(K[-1][0]*(K[0][1]-K[-2][1]))
suma += P
suma=0.5*abs(suma)  
print("%.3f"%suma) 