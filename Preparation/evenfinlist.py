
#Find the odd/even from list.
l= [10, 21, 4, 45, 66, 93] 
odd=[]
for item in l:
    if item % 2==0:
        odd=odd+[item]
print("odd list=",odd)
