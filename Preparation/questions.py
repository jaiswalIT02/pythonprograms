"""
def reverseWord(text):
    
    l=list(text)
    print(l)
    reverse=[]
    for item in l:
        reverse=[item] + reverse
    reverse="".join(reverse)
    return reverse
text=reverseWord("to reverse")
print(text)


def less_than_or_equal_to_zero(num):
  if num<=0:
      return True
  if num>=0:
      return False
x=less_than_or_equal_to_zero(-2)
print(x)


def return_negative(n):
    if n<=0:
        return n
    else:
        return -n
x=return_negative(77)
print(x)
# Python program to print even Numbers in a List 
  
# list of numbers 
l = [10, 21, 4, 45, 66, 93] 
  
# using list comprehension 
even_no = [num for num in l if num % 2 == 0] 
  
print("Even numbers in the list: ", even_no)


# Python program to print positive Numbers in a List 
  
# list of numbers 
list1 = [10, -21, 4, -45, -66, -93] 
  
# using list comprehension 
positive_nos = [num for num in list1 if num <= 0] 
  
print("positive numbers in the list: ", positive_nos)

#Remove multiple elements from list

l=[3,5,7,4,8,4,3]
l.sort()
print("l=",l)
"""

"""
"""
"""
#Find the reverse of given list.
l=[1,2,3,4]
l.reverse()
print(l)

"""












