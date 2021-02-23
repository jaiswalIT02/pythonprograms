def cube_naturalno(n):
    x=0
    for i in range(1,n+1):
        x+=i*i*i
    return x
n=cube_naturalno(5)
print(n)


def sumOfSeries(n): 
    sum = 0
    for i in range(1, n+1): 
        sum +=i*i*i 
          
    return sum
  
   
# Driver Function 
n = 5
print(sumOfSeries(n)) 
  