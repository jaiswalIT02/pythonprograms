l=[1,1,1,1,1,1,1,1,2,2,3,4,4,4,5,6,6,7]
l.sort()
c=l.count(1)
print("1 is =",c)
n=len(l)
newl=[l[0]]
for i in range(1,n):
    if l[i-1]!=l[i]:
        newl=newl + [l[i]]
print(newl)



