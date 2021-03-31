


n=4
x=1
for i in range(1,n+1):
    for j in range(1,n-i+1):
      print(x,end="")
      x=x+1
    print()


n=4
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
      print(x,end="")
      x=x+1
    print()



for i in range(1,6):
    for j in range(1,i+1):
         print("*",end="")
    print("")

for i in range(5,0,-1):
    for j in range(1,i+1):
         print("*",end="")
    print("")



for i in range(1,6):
    for j in range(1,6-i+1):
        print(" ",end="")
    for j in range(1,i+1):
         print("*",end="")
    print(" ")


n=5
for i in range(1,n+1):
    
    for j in range(1,n-i + 1):
        print(" ",end="")
    for j in range(1,i+1):
        print("0",end="")
    print()



n=5
for i in range(1,n+1):
    #print(i,end="")
    for j in range(1,n-i+1):
        print("0",end="")
    print()


n=5
for i in range(1,n+1):
    
    for j in range(1,n-i + 1):
        print(" ",end="")
    for j in range(1,i+1):
        print("0",end="")
    print()





