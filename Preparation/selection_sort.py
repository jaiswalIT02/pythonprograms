
l=[10,6,8,2,1]
n=len(l)
#This is method of selection sort..

for i in range(n-1):
    min=l[i]
    pos=i
    for j in range(i,n):
        if l[j]<min:
            min=l[j]
            pos=j
        t=l[i]
        l[i]=l[pos]
        l[pos]=t
print(l)

