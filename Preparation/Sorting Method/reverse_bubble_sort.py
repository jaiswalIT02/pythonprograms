l=[1,3,2,5,4]
n=len(l)
print("l=",l)
for i in range(n-1,0,-1):
    for j in range(n-1,0,-1):
        if l[j]>l[j-1]:
            t=l[j]
            l[j]=l[j-1]
            l[j-1]=t
print("Reversed list=",l)
 