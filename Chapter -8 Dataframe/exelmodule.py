
#import numpy as np
#import pandas as pd
#import numpy as np

def listtostr(l):
    s=str(l[0])
    for i in range(1,len(l)):
        ch=str(l[i])
        s=s + "," + ch
    return s


def strtolist(s):
    l=s.split(",")
    outputlist=[]
    for item in l:
        outputlist=outputlist + [int(item)]
    return outputlist

def SaveToExcel(player1,player2,board,currentplayer,gamestatus,excelfile):
  
    data={"data":[player1,player2,board,currentplayer,gamestatus]}
    index=["player1","player2","board","currentplayer","gamestatus"]
   
    df=pd.DataFrame(data,index)
    print(df)
    df.to_excel(excelfile)

def ReadFromExcel(excelfilename):
   df=pd.read_excel(excelfilename,index_col=0)
   # print(df)
   players=df["data"]
   player1=players[0]
   player2=players[1]
   board=players[2]
   currentplayer=players[3]
   gamestatus=players[4]
      
   return player1,player2,board,currentplayer,gamestatus


"""
filename=input("Enter the filename ")
filename ="F:\\game\\" + filename + ".xlsx"
player1,player2,board,currentplayer,ganestatus=ReadFromExcel(filename)
print(player1,player2,board,currentplayer,gamestatus)
"""