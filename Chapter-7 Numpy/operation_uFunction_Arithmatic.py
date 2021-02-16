import numpy as np

d1 = np.array([1,2,3,4])
d2 = np.array([5,6,7,8])

result =np.add( d1, d2)

print("add\n",result)
result =np.subtract( d1, d2)

print("subtract\n",result)
result =np.multiply( d1, d2)

print("multiply\n",result)
result =np.divide( d2, d1)

print("divide\n",result)

result =np.floor_divide( d2, d1)

print("floor divide\n",result)

result =np.power( d1, d2)

print("power\n",result)

result =np.remainder( d1, d2)

print("remainder\n",result)

result =np.divmod( d2, d1)

print("divmod\n",result)


result =np.absolute( d1)*-1

print("-abs\n",result)

result =np.trunc(  d2/d1)

print("trunc\n",result)
result =np.around(  d2/d1,2)

print("around\n",result)
result =np.floor(  d2/d1)

print("floor\n",result)
result =np.ceil(  d2/d1)

print("ceil\n",result)
result =np.ceil(  d1/d2)
print("Original\n",d1/d2)
print("ceil\n",result)
result =np.log(  d1)

print("log\n",result)
result =np.log10(  d2/d1)

print("log10\n",result)