def prime(x):
    limit=x**.5
    limit=int(limit)
    for i in range(2,limit+1):
        if x%i==0:
            return False
    return True
    
    print("Not prime")
        
a=int(input("N="))
result=prime(a)
print(result)
