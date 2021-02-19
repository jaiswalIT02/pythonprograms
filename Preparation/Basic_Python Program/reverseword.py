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