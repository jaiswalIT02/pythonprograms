def unlimitedAdd(*numbers):
    sum=0
    for x in numbers:
        sum=sum+x
    return sum


x=unlimitedAdd()
print(x)
x=unlimitedAdd(1)
print(x)
x=unlimitedAdd(1,2)
print(x)
x=unlimitedAdd(1,2,3)
print(x)
x=unlimitedAdd(1,2,3,4)
print(x)


