def leftrotate(str):
    l=list(str)
    n=len(l)
    t=l[n-1]
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
    l[0]=t
    result="".join(l)
    return result
str="TIGER"
str=leftrotate(str)
print(str)