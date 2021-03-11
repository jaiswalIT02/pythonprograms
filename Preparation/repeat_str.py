manas="manas is going from varanasi to to delhi and then from delhi to chandigarh"

l=manas.split()
print(l)

dic=dict.fromkeys(l,0)
print(dic)

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
