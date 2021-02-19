
"""
l=[1,2,3,4,5]
result="not exists"
v=3

for i in l:
    if i==v:
        result="exists"
        break
print(result)


#diction creating ways
l=[1,2,3,4,5,6,3]
s=set(l)
dic=dict.fromkeys(s,0)
print(dic)
"""

l=[1,2,3,4,5,6,6,3]
s=set(l)
dic=dict.fromkeys(s,0)
print(dic)
for item in l:
    dic[item]+=1
print(dic)
