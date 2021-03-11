def quicksort(a,left,right):
    if left>=right:
        return
    pivot=a[left]
    fp=left
    n=right+1
    for i in range(left+1,n):
        if a[i]>=pivot:
            continue
        fp+=1
        t=a[i]
        a[i]=a[fp]
        a[fp]=t
    t=a[left]
    a[left]=a[fp]
    a[fp]=t
    #print(a[left:right+1],left,right)
    quicksort(a,left,fp-1)
    quicksort(a,fp+1,right)


a=[10,11,1,5,17,7,11,10,8]
quicksort(a,0,len(a)-1)
print(a)