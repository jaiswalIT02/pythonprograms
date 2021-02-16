l=[1,3,5,9,10,15,2,7,9,16,23,29,35,7,11,10,13,2]
l=l+[0]
maxlength=0
maxlist=[]
n=len(l)-1
current=[]
for i in range(n):
    x=l[i]
    y=l[i+1]
   #print(x,",",end="")
    
    current=current + [x]
    if x>=y:
        if(len(current)>maxlength):
            maxlength=len(current)
            maxlist=list(current)
        print(current,len(current))
        current=[]
print("Max list= ",maxlist)


