"""
num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  

"""


n = 407  # int(input("enter a num="))
copy = n
sum = 0
while copy > 0:
    remain = copy % 10

    copy //= 10
    sum += remain ** 3

if n == sum:
    print(n, "is armstrong no")
else:
    print(n, "is not armstrong")
