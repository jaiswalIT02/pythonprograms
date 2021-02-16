l=[5,1,4,4,3,3,9,8,8,9,9]

l.sort()
print(l)
n=len(l)
print(n)
duplicatelist=[]
prev=l[0]

for i in range(1,n):
    curr=l[i]
    if curr==prev:
        if not prev in duplicatelist:
            duplicatelist=duplicatelist+[prev]
    prev=curr
print(duplicatelist)