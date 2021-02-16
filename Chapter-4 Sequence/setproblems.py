# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:32:43 2020

@author: Tarun Jaiswal
"""


x=range(2,10,2)

s=set(x)
print("s=",s)
#print(type(s))
#print(type(x))

y=range(4,20,4)

s1=set(y)
print("s1=",s1)
#print(type(s1))
#print(type(y))

ss1=s.issubset(s1)
print("subset=",ss1)

ss1=s.issuperset(s1)
print("superset=",ss1)

ss1=s.symmetric_difference(s1)
print("symmetric_difference=",ss1)

ss1=s.intersection(s1)
print("intersection=",ss1)

ss1=s.isdisjoint(s1)
print=("isdisjoint=	",ss1)	

