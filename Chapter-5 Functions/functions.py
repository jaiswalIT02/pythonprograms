def f_to_c(f):
    celcius=(f-32)*(5/9)
    return celcius


n=int(input("Farhenheite="))
c=f_to_c(n)
print(c)

      