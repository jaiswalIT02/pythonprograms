

class book:
    def __init__(self,bookname,price):
        self.bookname=bookname
        self.price=price
    def __str__(self):
        return "bookname={0},price={1}".format(self.bookname,self.price)

x=book("Java",300)
print(x)