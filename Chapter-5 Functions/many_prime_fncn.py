def prime(x):
    limit=x**.5
    limit=int(limit)
    for i in range(2,limit+1):
        if x%i==0:
          return False
    return True
    
sno=1
n=int(input("N="))
for i in range(2,n-1):
    result=prime(i)
    if result:
        print(sno," = ",i,end="\n")
        sno=sno+1

    
