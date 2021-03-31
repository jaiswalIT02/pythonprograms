# First Method ======================================
n=3
n_list=[[0 for x in range(n)] for y in range(n)]
#print(n_list)
num=1
low=0
high=n-1
count=int((n+1)/2)

for i in range(count):
    for j in range(low,high+1):
        n_list[i][j]=num
        num=num+1

    for j in range(low+1,high+1):
        n_list[j][high]=num
        num=num+1
    for j in range(high-1,low-1,-1):
        n_list[high][j]=num
        num=num+1
    for j in range(high-1,low,-1):
        n_list[j][low]=num
        num=num+1
    low=low+1
    high=high-1

for i in range(n):
    for j in range(n):
        print(n_list[i][j],end="  ")
    print()

# Second method ==========================
n=3
l=[]

for i in range(n):
    row=[]
    for j in range(n):
        row=row + [0]
    l=l+[row]


left=0
right=n-1
top=0
bottom=n-1
count=0
while count<n*n:
    for i in range(left,right+1):
        count+=1
        l[top][i]=count
    top+=1
    for i in range(top,bottom+1):
        count+=1
        l[i][right]=count
    right-=1
    for i in range(right,left-1,-1):
        count+=1
        l[bottom][i]=count
    bottom-=1
    for i in range(bottom,top-1,-1):
        count+=1
        l[i][left]=count
    left+=1
for i in range(n):
    for j in range(n):
     print(l[i][j],end="\t")
    print()
