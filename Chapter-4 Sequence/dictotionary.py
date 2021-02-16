# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:09:23 2020

@author: Tarun Jaiswal
"""


dictone = {
  "Name=": "Tarun Jaiswal",
  "subject=": "Python",
  "Topic=": "Dictionary"}
print(dictone)


for x in dictone:
    print(x)
    
for x in dictone.values():
  print(x)
  
for x, y in dictone.items():
  print(x, y)

dictone = {
 "Name=": "Tarun Jaiswal",
  "subject=": "Python",
  "Topic=": "Dictionary"
}
dictone["color"] = "red"
print(dictone)




dictone.popitem()
print(dictone)


del dictone["Name="]
print(dictone)




dict1=dictone.copy()
print(dict1)



dicttwo = dict(dictone)
print(dicttwo)