import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
runs={"Sachin":100,"Pappu":420,"Saubhagya":1}
wickets={"Sachin":1,"Pappu":420}
data=[runs,wickets]
index=["Runs","Wickets"]
df=pd.DataFrame(data,index)
print(df)
df.to_excel("E:\\Excel\\Tarun.xlsx")

#x=pd.read_excel("E:\\Excel\\scores.xlsx")
#print(x)




