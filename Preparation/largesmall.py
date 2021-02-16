l = [4, 3, 5, 4, -3,10,2,33,98,4]
print(l)
min = l[0]
max = l[0]

n = len(l)

for i in range(1, n):
    curr = l[i]
    if curr < min:
        min=curr
    if curr>max:
        max=curr

print("Min=",min,"Max=",max)

