l=[1,3,4,4,1,5,5,6,7]
l.sort()
print(l)
n=len(l)

nonduplicatelist=[]
prev=l[0]

for i in range(1,n):
    curr=l[i]
    if curr==prev:
        print(curr)
        
    