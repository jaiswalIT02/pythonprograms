
word="boy"
print(word)
reverse=[]
l=list(word)
for i in l:
    reverse=[i]+reverse
reverse="".join(reverse)
print(reverse)



l=[1,2,3,4]
print(l)
r=[]
for i in l:
    r=[i]+r
print(r)