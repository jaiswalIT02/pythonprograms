n = 135
sum = 0
copy = n
length = len(str(n)) + 1
count = 0
while ( n != 0 ):

    count+=1
    r = n % 10
    position = length - count
    sum = sum + r**position
    n = n // 10
if copy == sum:
    print("Disarium")
else:
    print("Not Disarium")
    