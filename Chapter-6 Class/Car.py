class Car:
    def __init__(self,model,price):
        print("Constructor")
        self.model=model
        self.price=price
    def __str__(self):
        return "Model={0}, Price={1}".format(self.model,self.price)
        
c1=Car("Business Class Mercedes",1000)
print(c1)