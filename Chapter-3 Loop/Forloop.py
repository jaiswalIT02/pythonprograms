# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 10:06:06 2020

@author: Tarun Jaiswal
"""

x1=range(10)
print(x1)
x2=range(2,10)
print(x2)
x3=range(2,10,3)
print(x3)
print("X1=",end="")
for item in x1:
    print(item,end=",")
print("X2=")
for item in x2:
    print(item,end=",")
print("X3=",end="")
for item in x3:
    print(item,end=",")
