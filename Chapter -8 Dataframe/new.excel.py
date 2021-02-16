import numpy as np
import pandas as pd
import numpy as np


def SaveToExcel(player1,player2,board,currentplayer,gamestatus,excelfile):
  
    data={"data":[player1,player2,board,currentplayer,gamestatus]}
    index=["player1","player2","board","currentplayer","gamestatus"]
   
    df=pd.DataFrame(data,index)
    print(df)
    df.to_excel("E:\\game\\data.xlsx")

def ReadFromExcel(excelfilename):
    df=pd.read_excel(excelfilename,index_col=0)
    print(df)
    players=df["data"]
    player1=players[0]
    player2=players[1]
    board=players[2]
    currentplayer=players[3]
    gamestatus=players[4]
   # player1=players["player1"]
    
    return player1,player2,board,currentplayer,gamestatus
x1=ReadFromExcel("E:\\game\\data.xlsx")
print(x1)

"""
player1="Pappu"
player2="Pippi"
result="Won" 

tictactoe=[0]
currentplayer=0
board ="0,0,0,0,0,0,0,0,0"
players=[player1,player2,board,currentplayer]#Make a list of the data

   
print(players)
print(currentplayer)

data={"players":players}#Create a dictionary of the data
index=["Player1","Player2","Board","currentplayer","Result"]#Create an index

Loss={"Player1":Pappu,"Player2":Pippi}
data=[Won,Loss]
index=["Won","Loss"]

df=pd.DataFrame(data)
#print(df)
df=pd.DataFrame(data,index)#Create the dataframe
print(df)

df.to_excel("E:\\excel\\game.xlsx")
"""
#SaveToExcel("Kishan","Tarun", "2,0,2,0,1,1,1,0","0","0","E:\\game\\sthghghatus.xlsx")



