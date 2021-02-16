l=[1,1,0,0,0,1,0]
print(l)
l=l+[0]
n=len(l)
print(l)
for i in range(1,n-1):
    item1=l[i-1]
    item2=l[i]
    if(item1!=item2):
        print()
    print(item2,",",end="")
    
x=0
y=2
l=y-x
print(l)
x=2
y=5
l=y-x
print(l)
x=5
y=6
l=y-x
print(l)
x=6
y=7
l=y-x
print(l)
