n=5
for row in range(0,n+1):
    val=row+1
    dec=n-1
    for col in range(1,row+1):
        print(val,end=" ")
        val=val+dec
        dec=dec-1
    print()