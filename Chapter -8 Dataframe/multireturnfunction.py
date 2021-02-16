def multireturn():
    return 1,2,3


def maxmin(a,b):
    if a>b:
        return a,b
    else:
        return b,a
x=multireturn()
print(x, type(x))

a,b,c=x
print(a,b,c)
l=[1,2,3]
a,b,c=l
print(a,b,c)

max,min=maxmin(3,22)
print(max,min)