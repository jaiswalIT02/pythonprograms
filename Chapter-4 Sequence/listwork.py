# Create a list of odd numbers, even numbers

#Create a list of factorials
#Find the last 5 numbers from beginning to end in a series
#Find all odd numbers in a list
#merge 2 lists by removing common elements




l1=[1,3,2,3,4]
l2=[3,3,4,5,6,9]
l=[]
for item in l1:
    if item not in l:
        l=l + [item]
        
for item in l2:
    if item not in l:
        l=l + [item]
        
print(l)



