"""

for num in range(1,10):
    if all(num%i!=0 
           for i in range(2,num)):
        print(num)
        
   
# Find the reverse eliment in list:
l=[1,5,3,78,98,45,56,23,89,169,344]
l.sort(reverse=True)
print(l)


"""


# Find the fibbonacy series:
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
    
for i in range(0,12):
    print(f(i))

l=[i]
print(l)




# number of words in a given sentenc
s='I am doing programming.'
print(len(s.split()))
    