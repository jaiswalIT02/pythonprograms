"""
l=[3,4,5,6,7,8]
n=len(l)
print(l,n)
n=int(input("Enter the no="))
if n in l:
    print("yes")
else:
    print("no")

"""

l=[4,7,3,7,9]

result="not found"
search=7
for item in l:
    if search==item:
        result="Found"
        break
print(item)