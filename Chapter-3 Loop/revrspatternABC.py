n=5
x=1

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
       
    for k in range(1,i+1):
        ch=chr(ord('A')+k-1)
        print(ch,end="")    
    for k in range(i-1,0,-1):
        ch=chr(ord('A')+k-1)
        print(ch,end="")
        x=x+1
    print()
    


'''
n=5
x=1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
       
    for k in range(1,i+1):
        ch=chr(ord('A')+j-1)
        print(ch,end="")    
    for k in range(i-1,0,-1):
    
        print(ch,end="")
        x=x+1
    print()
'''