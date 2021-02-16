
def factorial(n):
    fact=1
    for i in range(1,n+1):  
        fact=fact*i
    return fact

def nCr(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


    
print(nCr(5,3))


