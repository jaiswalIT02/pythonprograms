import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas as pd
#import numpy as np
#import pandas as pd 


#from scipy import stats
#import matplotlib.pyplot as plt
def strtolist(s):
    l=s.split(",")
    outputlist=[]
    for item in l:
        outputlist=outputlist + [float(item)]
    return outputlist


"""
x = [4,5,6,7]
y = [410,420,435,440]

data={"poly":[x,y]}
index=["x","y"]
df=pd.DataFrame(data,index)
print(df)
df.to_excel("F:\\Excel2\\new.xlsx")

1,2,3,4,5,

1,4,2,4,4,5,2,5
1,2,2,4,4,4,5,5
 4 duplicates
 
 3,6,7,8
 1,2,4,5
 
 



"""
def readexcel(excel):
    df=pd.read_excel(excel)
    #print(df)
    polynomial=df["poly"]
    x=polynomial[0]
    y=polynomial[1]
    return x,y
x,y=readexcel("F:\\Excel2\\poly.xlsx")
print(type(x),y)
x=strtolist(x)
y=strtolist(y)
print(numpy.linspace(1,101,11))
model = numpy.poly1d(numpy.polyfit(x, y, 2))
print(model)
print(numpy.polyfit(x, y, 1))
correlation=r2_score(y, model(x))
print("Correlation",correlation)
plt.scatter(x,y,color="Black")
plt.plot(x,y,"b-",label="Original")
plotx=[1,2,3,4,5]
plt.plot(plotx, model(plotx),"r-",label="Predicted")
plt.ylabel('Y')
plt.xlabel('X')

plt.legend()
plt.show()
xvalue=4
predict=model(xvalue)
print(predict)


