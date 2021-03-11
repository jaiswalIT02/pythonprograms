a=[6,5,4,3,2,1,0]
n=len(a)
print("old array=",a)
for i in range(n-1):
    if a[i]<a[i+1]:
        continue
    t=a[i+1]
    j=i+1
    while j>=1 and a[j-1]>t:
        a[j]=a[j-1]
        j=j-1
    a[j]=t
print("New array=",a)
