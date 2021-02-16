# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:03:28 2020

@author: Tarun Jaiswal
"""

a=int(input("Enter the first no="))
b=int(input("Enter the second no= "))
c=int(input("Enter the third no="))

print("a={0}".format(a))
print("b={0}".format(b))
print("c={0}".format(c))
   
if a>=b and a>=c:
    max=a
else:
    if b>=c:
     max=b
    else:
     max=c
print(max)