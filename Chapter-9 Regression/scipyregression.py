import numpy as np
import pandas as pd

from scipy import stats
import matplotlib.pyplot as plt
x = [4,5,6,7]
y = [423,428,435,440]

data=[x,y]
index=["x","y"]
df=pd.DataFrame(data,index)
print(df)
df.to_excel("F:\\Excel2\\poly.xlsx")




#x=pd.read_excel("F:\\Excel2\\regret.xlsx")
#print(x)
#x=pd.read_excel("F\\Excel2\\regret.xlsx",index_col=0)
#print(x)

slope, intercept, r, p, std_err = stats.linregress(x, y)

def linefunc(x):
  return slope * x + intercept

model = list(map(linefunc, x))
print("model",model)
print(r)
xvalue=10
predictedy=linefunc(xvalue)
print("Y=",predictedy)
plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x, model)
plt.show()
