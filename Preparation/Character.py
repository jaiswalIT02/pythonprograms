
"""
0-25 
1-24
2-23
3-22
x=25-x
"""
ch = 'm'
Aascii = ord('a')
chrascii = ord(ch)
print(chrascii)
diff = chrascii-Aascii
print(diff)
reversediff = 25-diff
print(reversediff)
reverseascii = reversediff + Aascii
print(reverseascii)
reversechar = chr(reverseascii)
print(reversechar)