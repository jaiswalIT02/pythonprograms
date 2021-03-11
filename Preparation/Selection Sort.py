
l=[10,6,8,2,1]
n=len(l)
position=3

for i in range(position):
    min=l[i]
    pos=i
    for j in range(i,n):
        if l[j]<min:
            min=l[j]
            pos=j
        t=l[i]
        l[i]=l[pos]
        l[pos]=t
print(l[position-1])
print(l)

