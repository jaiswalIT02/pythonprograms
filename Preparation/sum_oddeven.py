l=[3,4,5,6,7]
print(l)
oddsum=0
evensum=0


for i in l:
    if i%2!=0:
        oddsum=oddsum+i
    else:
        evensum=evensum+i
print("odd list=",oddsum,"even list=",evensum)

   
