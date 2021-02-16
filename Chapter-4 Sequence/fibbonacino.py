# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:15:18 2020

@author: Tarun Jaiswal
"""

a=0
b=1
n=5
for i in range(n):
    print(a)
    temp=a
    a=b
    b=temp+b
    print(b,end=",")
    
    