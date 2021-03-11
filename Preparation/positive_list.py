#find the positive no from list
l1= [10, -21, -4, -45, -66, 93]
positive=[]
for item in l1:
    if item >= 0:
        positive=positive+[item]

print("positive list=",positive)
