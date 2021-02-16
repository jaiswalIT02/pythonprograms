def pad(n):
        if(n>=10):
            return "" + str(n)
        return "0" + str(n)

class Time:
    
    def __init__(self,hour,minute):
        self.hour=hour
        self.minute=minute
        
    
    def __str__(self):
        if self.hour<=11:
            return "{0}:{1} AM".format(pad(  self.hour),pad(self.minute))
        if self.hour==12:
            return "{0}:{1} PM".format(pad(  self.hour),pad(self.minute))
        return "{0}:{1} PM".format(pad(  self.hour-12),pad(self.minute))
    
for hr in range(0,24):
    for min in range(0,60):
        t=Time(hr,min)
        print(t,end=",")    