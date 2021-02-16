l=[]
x,y=34,21

print(x,",",y,",",end="")      
z=x-y
while(z>0):
    print(z,",",end="")
    x=y
    y=z
    z=x-y
print(0)

l=l+[]
print(l)

