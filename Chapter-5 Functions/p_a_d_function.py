def rectangle(l,b):
    
    perimeter=2*l + 2*b
    area=l*b
    diagonal=(l*l + b*b)**0.5
    return perimeter,area,diagonal



p,a,d=rectangle(3,4)
print("Perimeter=",p,"cm","area=",a,"cm2",d)