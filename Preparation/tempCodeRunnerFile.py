# Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
l = [10, 20, 4, 45, 99, 89, 78, 109]

mx = max(l[0], l[1])
secondmax = min(l[0], l[1])
n = len(l)
for i in range(2, n):
    if l[i] > mx:
        secondmax = mx
        mx = l[i]
    elif l[i] > secondmax and \
            mx != l[i]:
        secondmax = l[i]