# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:03:57 2020

@author: Tarun Jaiswal
"""

n=5
x=1
for i in range(1,n+1,1):
    for j in range(i,0,-1):
        
         ch=chr(ord('A')+j-1)
         print(ch,end="")
    x=x+1
    print()
    

