# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:25:48 2020

@author: Tarun Jaiswal
"""


a=int(input("Enter the first no="))
b=int(input("Enter the second no= "))
c=int(input("Enter the third no= "))
if a<b or a<c:
    if b<c:
        max=c
    else:
        max=b
else:
    max=a
    
print(max)
    
