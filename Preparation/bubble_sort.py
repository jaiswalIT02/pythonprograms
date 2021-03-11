l=[10,9,2,8,4]
n=len(l)
print(l)
for i in range(n-1):
    for j in range(n-1-i):
        if l[j]>l[j+1]:
            t=l[j]
            l[j]=l[j+1]
            l[j+1]=t
print("arranged list=",l)

