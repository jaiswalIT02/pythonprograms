n=6
x=1
for i in range(1,n+1):
    for j in range(i,0,-1):
        ch=chr(ord('Z')-j+1)
        print(ch,end="")
        x=x+1
    print()

for i in range(n,0,-1):
    for j in range(i,0,-1):
        ch=chr(ord('Z')-j+1)
        print(ch,end="")
        x=x+1
    print()
