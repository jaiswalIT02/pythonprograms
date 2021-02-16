

a=int(input("A= "))
b=int(input("B= "))
c=int(input("C= "))

max=a
min=a

if b>max:
    
    max=b
    
if b<min:
    
    min=b
    
if c>max:
    
    max=c
    
if c<min:
    
    min=c
    
print("Max = ",max)   
print("Min = ",min)
mid=a+b+c-max-min
print("Mid = ",mid)

