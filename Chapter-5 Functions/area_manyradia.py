def area(r):
    area=3.14*r**2
    return area

n=int(input("radius="))
for i in range(1,n+1):
    
    result=area(i) 
    print("area=",result,"cm2") 
  