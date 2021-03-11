l=[2,2,4,6,9,13,13,4,4]
max=[0]
s=set(l)
print("s=",s)
dic=dict.fromkeys(s,0)
print("dic=",dic)

for i in l:
    dic[i]+=1
print("NewDic=",dic)

max=0
pos=0

for key in dic.keys():
    value=dic[key]
    if (value > max) :
        max=value
        pos=key
print("No of repeats=",max)

for key in dic.keys():
    value=dic[key]
    if value == max:
        print("Max repeated element=",key)

    