x = 5
y = 10
"""
x, y = y, x
print( x,y)
"""


print(x, y)
temp = x
x = y
y = temp

print(x, y)

# without any other variable.

x = x+y

x = x-y
print(x, y)
