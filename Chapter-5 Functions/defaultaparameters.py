def defaultValueParameters(a=0,b=0):#Default value of a is 0 and b is 0
    sum=a+b
    return sum
x=defaultValueParameters()#a=0 and b=0 is not given
print(x)
x=defaultValueParameters(1)#a=1 and b=0
print(x)
x=defaultValueParameters(1,2)#a=1 and b=2
print(x)

