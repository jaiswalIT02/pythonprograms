import numpy as np
d1=np.array([1,2,3,4,5,6])
print(d1)
searcharray=[True,False,True,False,True,False]
result=d1[searcharray]
print("Result",result)
searcharay= d1%2==0
result=d1[searcharray]
print("result",result)
searcharray=d1%2!=0
result=d1[searcharray]
print("result",result)
d1=np.array([[1,2,3],[4,5,6]])
seacharray=[True,False,True,False,True,False]
seacharray=np.reshape(searcharray,(2,-1))
print(d1)
print(searcharray)
result=d1[searcharray]
print("Result",result)

#where returns the index
d1=np.array([1,2,3,4,5,6])
result=np.where(d1%2==0)
print("Result",result)





