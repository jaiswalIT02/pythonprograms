# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:21:13 2020

1,-2,3,-4....
@author: Tarun Jaiswal

"""
n=int(input("Enter the no="))
x=range(11,1,-1)
print(x)
for item in x:
    
    if item % 2==0:
        print(n*item)
    else:
        print(item*n)
        

