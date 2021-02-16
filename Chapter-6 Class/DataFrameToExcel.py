import numpy as np
import pandas as pd

runs={"Sachin":100,"Pappu":420,"Saubhagya":1,"Dhoni":30}
wickets={"Sachin":1,"Pappu":420,"Saubhagya":9}
data=[runs,wickets]
index=["Runs","Wickets"]
df=pd.DataFrame(data,index)
print(df)

df.to_csv("F:\\excel\\scores.csv")

df.to_excel("F:\\excel\\scores.xlsx")

x=pd.read_csv("F:\\excel\\scores.csv")
print(x)

x=pd.read_csv("F:\\csv\\scores.csv",index_col=0)
print(x)
x=pd.read_excel("F:\\csv\\scores.xlsx")
print(x)
x=pd.read_excel("F:\\csv\\scores.xlsx",index_col=0)
print(x)
