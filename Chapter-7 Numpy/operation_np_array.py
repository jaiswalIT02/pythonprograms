import numpy as np
print(3**2)
d11=np.array([1,2,3,4,5,6])
d12=np.array([3,4,5,6,7,8])
d21=np.array([[1,2,3],[4,5,6]])
d22=np.array([[3,4,5],[6,7,8]])
result = np.add(d11, d12)
print("Sum {0} + {1} = {2} ".format(d11,d12,result))
result=d11*d12
print("Product {0} X {1} = {2} ".format(d11,d12,result))
result=d11/d12
print("Divide {0} / {1} = {2} ".format(d11,d12,result))
result=d11//d12
print("Divide {0} // {1} = {2} ".format(d11,d12,result))
result=d11**d12
print("Product {0} XX {1} = {2} ".format(d11,d12,result))
result=d11%d12
print("Product {0} % {1} = {2} ".format(d11,d12,result))

result=1/d12
print("Reciprocal {0} /X {1} = {2} ".format(1,d12,result))
x=np.ones(6,int)
print("Reciprocal {0} /X {1} = {2} ".format(x,d12,result))
result=d11**(-1/1)
print("Reciprocal {0} = {1} ".format(-1,result))


