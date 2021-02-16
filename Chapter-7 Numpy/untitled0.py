import numpy as np

d1 = np.array([1,2,3,4])
d2 = np.array([5,6,7,8])
d3=np.array([[1,2],[3,4]])
result=np.add(d1,d2)
print("Add",result)
result=np.add(d3,d3)
print("Add",result)
result=np.cumsum(d1)
print("Cumulative Sum",d1,result)
result=np.prod(d1)
print("Prod",d1,result)
result=np.prod([d1,d2])
print("Prod",d1,d2,result)
result=np.prod([d1,d2],axis=0)
print("Prod",d1,d2,result)
result=np.prod([d1,d2],axis=1)
print("Prod",d1,d2,result)

result=np.cumprod([d1])
print("CumProd",d1,result)
x=[1,3,44,5,66]
result=np.diff([x])
print("Diff",x,result)
result=np.diff([x],2)
print("Diff",x,result)
result=np.diff([x],len(x)-1)
print("Diff",x,result)
result=np.lcm.reduce(d2)
print("GCD",d2,result)
result=np.gcd.reduce(d2)
print("GCD",d2,result)