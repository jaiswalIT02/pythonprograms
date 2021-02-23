#
n=int(input("Enter no="))
sum=0
copy=n
while copy > 0:
    digit=copy % 10
    copy //= 10
    sum+= digit ** 2

    
if sum==n:
    print(n,"is happy no")
else: 
    print(n,"is not happy no")

