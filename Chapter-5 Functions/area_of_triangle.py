def a_of_triangle(a):
    s=a+b+c
    area=(s-a)*(s-b)*(s-c)/2
    return area


a=int(input(("A=")))
b=int(input(("B=")))
c=int(input(("C=")))

area=a_of_triangle(a)
print("area=",area,"cm2")