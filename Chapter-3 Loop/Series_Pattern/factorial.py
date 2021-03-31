# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:19:40 2020

@author: Tarun Jaiswal
"""


l=[]
i=1
fact=1
n=5
for item in range(1,n+1):
  fact=fact*i
  l=l+[fact]
  i=i+1

print(l)

