def fibbonaci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    a=0
    b=1
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
    return c

for i in range(1,15):
    f=fibbonaci(i)
    print(f,",",end="")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    