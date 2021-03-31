'''
n=0
r=4
for m in range(1,r+1):
    for gap in range(1,(r-m)+1):
        print(end=" ")
    while n!=(2*m-1):
        print("0",end=" ")
        n=n+1
    n=0
    print()
'''
n=int(input("Enter the n="))
k=(2*n)-2

for i in range(1,n):
    for j in range(1,k):
        print(end=" ")
    k=k-1
    for n in range(1,i+1):
        print("0",end=" ")
    print(" ")
    


    