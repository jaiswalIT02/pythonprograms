# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:10:16 2020

@author: Tarun Jaiswal
"""


n=5
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print(i,end="")
    print()
for i in range(2,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print(i,end="")
    print()
    
    
