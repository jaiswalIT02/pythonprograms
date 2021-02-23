l = [43, 3, 5, 4, 78]
"""
print(l)
max = l[0]

for item in l:
    curr = item
    if curr>max:
        max=curr

print("Max=",max)



max = l[0]
for i in l:
    if i > max:
        max = i
print("max=", max)

"""

max1 = l[0]
max2 = l[1]
for i in l:
    if i > max1:
        max2 = max1
        max1 = i

    if max1 > max2 and max1 != i:
        max2 = i
print("max1=",max1,"max2=", max2)



min1 = l[0]
min2 = l[1]
for i in l:
    if i < min1:
        min2 = min1
        max1 = i

    if min1 < min2 and min1 != i:
        max2 = i
print("min1=",min1,"min2=", min2)
