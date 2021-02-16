
import pandas as pd
#from sklearn import linear_model

#from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

#import pandas as pd
def readexcel(excel):
    df=pd.read_excel(excel)
   
    return df
df = readexcel("F:\\Excel2\\Market.xlsx")
#print(df)

x = df[['phy','chem' ]]
y = df['division']
print(x)
print(y)

dtree = DecisionTreeClassifier()
print(dtree)
dtree = dtree.fit(x, y)
print(dtree)

result=dtree.predict([[80,75]])
print(result)

result=dtree.predict([[39,45]])
print(result)
"""
result=dtree.predict([[250,2500]])
print(result)
result=dtree.predict([[50,50]])
print(result)
"""