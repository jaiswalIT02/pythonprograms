# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:19:26 2020

@author: Tarun Jaiswal
"""


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

for x in set3:
    print(x)
    
    
s1={"x","y","z"}
s2={1,2,3,4}


s1.update(s2)
print(s1)