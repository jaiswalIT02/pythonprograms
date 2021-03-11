
"""
for item in l:
    curr = item
    if curr<min:
        min=curr
"""

l=[3,8,2,1,4]
min=l[0]
pos=0
print(l)
for i in range(len(l)):
    if l[i]<min:
        min=l[i]
    
        pos=i
t=l[i]
l[i]=l[pos]
l[pos]=t
print("min=",min,l)



"""
l[0],l[3]=l[3],l[0]
print(l)

"""