class person:
    def __init__(self,name,age):
        print("Identify")
        self.name=name
        self.age=age
    
    def __str__(self):
       #print("Hello my name is " + self.name)
        return "Name={0}, Age={1}".format(self.name,self.age)
    
p1 = person("Pappu",55)
print(p1)




