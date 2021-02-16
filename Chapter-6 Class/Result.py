class Result:
    def __init__(self,roll,name,physics,chemistry,math):
        self.roll=roll
        self.name=name
        self.physics=physics
        self.chemistry=chemistry
        self.math=math
        
    def __str__(self):
        return "Roll={0},Name={1},Physics={2},Chemistry={3},Math={4},Total={5},Per={6},Division={7}".format(self.roll,self.name,self.physics,self.chemistry,self.math,self.total(),self.per(),self.division())
    
    def total(self):
        total= self.physics+self.chemistry+self.math
        return total
    
    def per(self):       
        if not self.isPass():
            return "---"
        per=round(self.total()/3,2)       
        return per
    
    def division(self):
         if self.per()<50:
           return "3rd"
         elif self.per()<60:
           return "2nd"
         else:
           print("1st")
           return "1st"
           
    def isPass(self):
        if self.physics<40 or self.chemistry<40 or self.math<40:
           return False
        else:
           return True
     
re=Result(15,"Pappu",56,50,65)  
print(re)

