def selection_sort(l): 
    n=len(l)
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
    return l
