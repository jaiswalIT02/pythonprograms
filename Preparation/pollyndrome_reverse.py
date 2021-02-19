#Pollyndrome/revers list both are printing

l = ['1', '2', '3']
l1=[]
for i in l:
    l1=[i]+l1+[i]
print("l=",l,"l1=",l1)
