x=34
if(x==0 or x==1):
    print(x,"Is fibonacci")
else:
    a,b=0,1
    c=a+b
    while(c<x):
        a=b
        b=c
        c=a+b
    if(c==x):
        print(x, "Is fib")
    else:
        print(x, "Not fib")
        