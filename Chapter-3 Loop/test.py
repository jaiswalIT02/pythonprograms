
n=5
x=0
for i in range(0,n+1):
    for j in range(1,i+1):
        x=(x+1)%26
        ch=chr(x-1+ord('A'))
        print(ch,end=" ")
        n=n+1
    print()