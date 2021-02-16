# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:43:44 2020

@author: Tarun Jaiswal

"""
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    
    for k in range(1,i+1):
         print(k,end="")    
   
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
