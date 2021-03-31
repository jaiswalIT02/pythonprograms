"""
print("\\n")

x="87654321"[::-1]
print(type(x))
print(x)


x=(round(4.5)-round(-4.5))
print(x)

print("0.5".isdecimal())


print('Aa'.isalpha())

x="python"+str("1"+"2"+"3")
print(x)

print('Aa'.maketrans('Aa','12'))
print( ord(' '))
print(chr(27))


for i in range(0,10):
    y = chr(i)
    print(i,"=",y,end=",")


for i in range("A","Z"):
   a=ord(i)
   print(a) 

# using lambda expression:


def sum(a, b):
    c = a+b
    return c


f = lambda a, b: a+b
r = f(3, 4)
print(r)

f = lambda n: 1 if n == 0 else n*f(n-1)
print(f(5))


print(lambda a,b:a-b(9,7))



#x=int(input("Enter no="))
n=3
for i in range(0,n):
    for j in range(1,n+1):
        print(i+j," ",end="")
    print()

n=ord("A")
for item in range(n,n+26,1):
      print(chr(item),end=" ")



str1 = "Tarun"  
x = ""
for i in str1:  
    x += i
    print(x)

x=12
for i in range(1,11):
    print(x*i)

n=3
for i in range(0,n):
    for j in range(1,n+1):
        print(i+j,end=" ")
    print()

for i in range(0,n):
    for j in range(0,n+1):
        print(j,end=" ")
    print()




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




w="Arbaj"
l=list(w)
n=len(l)
print(l,n)

ret="".join(l)
print(ret)


#n=3
#for i in range(0,n+1):
 #   for j in range(1,n+1):
  #    print(i,j,end="")
  #  print()

1   2  3  4
12 13 14  5
11 16 15  6
10  9  8  7



print("Tarun")


def rotate(str):
    n=len(str)
    l=list(str)
    chr=l[0]
    for i in range(0,n-1):
        l[i]=l[i+1]
    l[n-1]=chr
    return "".join(l)

input1=input()
input2=int(input("Enter="))
l1=input1.split()
n=len(l1)
l2=list(l1)
for i in range(0,n):
    word=l1[i]
    for j in range(input2):
        word=rotate(word)
    l2[i]=word
count=0
for i in range(n):
    if l1[i]==l2[i]:
        count+=1
print("Correct words is ",count)

temp=l[n-1]
l[4]=l[3]
l[3]=l[2]
l[2]=l[1]
l[1]=l[0]
l[0]=temp







# left rotate
def leftrotate(str):
    l=list(str)
    n=len(l)
    t=l[n-1]
    for i in range(n-1,0,-1):
        l[i]=l[i-1]
        
    l[0]=t
    result="".join(l)
    return result

str="CAR"
print(str)
str=leftrotate(str)

print(str)

"""
'''
# right rotate
str="CAT"
l=list(str)
n=len(l)
i=n-1
print(str)

l[0]=l[1]
l[1]=l[2]
print(l)


def rightrotate(str):
    l=list(str)
    n=len(l)
    t=l[n-1]
    for i in range(0,n-1):
        l[i]=l[i]
        
    l[0]=t
    result="".join(l)
    return result

str="CAT"
print(str)
str=rightrotate(str)
print(str)

'''