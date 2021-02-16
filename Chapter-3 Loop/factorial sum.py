
n=int(input("N= "))

x=range(1,n+1)
sum=0
fact=1
i=1
for item in x:
       fact=fact*item
       print("fact = ",fact)
       sum=sum + fact
print("Factorial Sum=",sum)
    