# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:50:21 2020

@author: Tarun Jaiswal
"""

a=0
b=1

n=10
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    # print(c)
 
    no=int(input("No="))
    if no<c or c>no:
      print(no,"is fibbonaci no.")
    else:
     print(no,"is not fibbonacy no.")


