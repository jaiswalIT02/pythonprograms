import pandas as pd
#from sklearn import linear_model

#from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

import pandas as pd
def readexcel(excel):
    df=pd.read_excel(excel)
   
    return df
df=readexcel("F:\\Excel2\\marks.xlsx")
print(df)


x = df[['Phy']]
y = df['Result']

print(y)
print(x)
dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)

for x in range(0,101):
    result=dtree.predict([[x]])
    print(x,"=",result,sep="",end=",")
"""
result=dtree.predict([[44,45]])
print(result)
result=dtree.predict([[100,39]])
print(result)
result=dtree.predict([[50,50]])
print(result)
"""

