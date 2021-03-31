
n=5
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        ch=chr(ord('A')+j-1)
        print(x,end="")
        x=x+1
    print()
    
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        ch=chr(ord('A')+j-1)
        print(x,end="")
        x=x+1
    print()
    
    
    
