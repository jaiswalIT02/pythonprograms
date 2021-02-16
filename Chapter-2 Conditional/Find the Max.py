# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:19:02 2020

@author: Tarun Jaiswal
"""
#Maximum in two no -

a=int(input("Enter the first no="))
b=int(input("Enter the second no= "))
print("a={0}".format(a))
print("b={0}".format(b))

if a>=b:
    print(a)
else:
    print(b)
    
    
  #Maximum in the no-
    

kiskavalue=""
a=int(input("Enter the first no="))
b=int(input("Enter the second no= "))
c=int(input("Enter the third no="))

print("a={0}".format(a))
print("b={0}".format(b))
print("c={0}".format(c))

if   a>=b:  
            max=a
            kiskavalue="a"
else:
   if b>=c:
            max=b
            kiskavalue="b"
            max=c
            kiskavalue="c"

else:
    if(b>=c):
        kiskavalue="b"
        max=b
    else:
        kiskavalue="c"
        max=c
        
print(kiskavalue, " = ",  max)





