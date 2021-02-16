

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:09:46 2020

@author: Tarun Jaiswal
"""
p=int(input("Physics="))
c=int(input("Chemistry="))
m=int(input("Mathematics="))


if p<40 or c<40 or m<40:
    print("Result=Fail")
else:
    print("Result=Pass")
    Total= p+c+m
    print("Total={0}".format(Total))
    per=round(Total/3,2)
    print("Per={0}".format(per))
    if per<50:
        print("3rd")
    elif per<60:
        print("2nd")
    else:
        print("1st")
