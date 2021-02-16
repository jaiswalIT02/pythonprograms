# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:49:48 2020

@author: Tarun Jaiswal
"""


a=range(8,48,8)
print(a)
for item in a:
    print(item)
s1=set(a)
print("A=",s1)

b=range(4,28,4)
print(b)
for item in b:
    print(item)
s2=set(b)
print("B=",s2)

s1s2=s1.symmetric_difference(s2)
print("symmetric_difference=",s1s2)

s1s2=s1.intersection(s2)
print("intersection=",s1s2)