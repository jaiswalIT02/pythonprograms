import pandas as pd
from sqlalchemy.sql.functions import min


def SaveToExcel(player1,player2,excelfilename):
    data={"name":[player1,player2]}
    index = ["player1", "player2"]
    df = pd.DataFrame(data, index)
    print(df)
   # df.to_excel(excelfilename)
   
#0,1,2,3
def ReadFromExcel(excelfilename):
    df=pd.read_excel(excelfilename,index_col=0)
    #print(df)
    players=df["name"]
    player1=players[0]
    player2=players[1]
    player1=players["player1"]
    return player1,player2
x1,x2=ReadFromExcel("E:\\Excel\\data.xlsx")
print(x1,x2)

"""
SaveToExcel("AB","CD","h:\\pandas\\data.xlsx")
player1="dffsdfsf"
player2="sadsdsad"
filename="h:\\pandas\\myfile.xlsx"
SaveToExcel(player1,player2,filename)

print("Hello")
data={"name":["pappu","pippi"]}
index=["player1","player2"]
print(data)
df=pd.DataFrame(data,index)
print(df)
df.to_excel("h:\\pandas\\data.xlsx")
"""



