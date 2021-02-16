def fibbonaci(n):
   # x,y=34,11
    z=x-y
    while (z>0):
        x=y
        y=z
        z=x-y
        return z
for i in range(144,8)    
f=fibbonaci(i)
print(f,",",end="")
    