a=int(input("A= "))

limit=a**.5
limit=int(limit)
isprime=True
for i in range(2,limit+1):
    if a % i==0:
        isprime=False
        break
if isprime:
    print("Prime")
else:
    print("NotPrime")
    

    