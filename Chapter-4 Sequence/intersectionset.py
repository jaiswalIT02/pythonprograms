# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:14:34 2020

@author: Tarun Jaiswal
"""

l=[1,2,3,4,3,4,5]
s=set(l)
print("set=",s)

a = {1,2,3}
b = {3,4,5}
ab=a.difference(b)
ba=b.difference(a)
print(ab)
print(ba)


