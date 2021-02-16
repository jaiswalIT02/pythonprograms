#use the curentobj instead of self:


class Person:
  def __init__(currentobj, name, age):
    currentobj.name = name
    currentobj.age = age

  def myfunc(xyz):
    print("Hello my name is " + xyz.name)

p1 = Person("Pappu", 55)
p1.myfunc()