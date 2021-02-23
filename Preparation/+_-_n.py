l=[-9,-86,56,-9,88]
positive=[]
negative=[]
for i in l:
    if i >= 0:
        positive=positive+[i]
    if i <= 0:
        negative=negative+[i]
print("positive list=",positive,"\nNegative List=",negative)