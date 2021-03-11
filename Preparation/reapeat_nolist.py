l=[1,2,3,5,3,4,2,7]
l.sort()
s=set(l)
dic=dict(s,0)
l=[]
print(l)
     



"""

l=[1,2,3,5,3,4,7,2]
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
"""











