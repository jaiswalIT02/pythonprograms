def even(x):
   if x%2==0:
       return True
   else:
   
      return False
sno=1    
n=int(input("N="))
for i in range(2,n-1):
    result=even(i)
    if result:
        print(sno," = ",i,end="\n")
        sno=sno+1

    
