#binary search method to check the elements in given list:......
l=[3,3,4,7,9,2,1,2,0,-6]
l.sort()
print(l)
left=0
right=len(l)-1
search=int(input("Search value="))
print("left = ",left ,",right=",right,l[left:right+1])
while True:
    mid=(left+right)//2
    if search==l[mid]:
        print("Found at ",mid)
        break
    if search<l[mid]:
        right=mid-1
    if search>l[mid]:
        left=mid +1
    print("left = ",left ,",right=",right,l[left:right+1])
    if left>right:
        print("Not found")
        break

l=[1,3,5,6,7,8]
l.reverse()
print(l)