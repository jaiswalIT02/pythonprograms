from Textblob import textblob
mylist=["Incorrect","spelling"]
corrected_list=[]
for word in mylist:
    corrected_list.append(Textblob(word))
print("Corrected list words are:")
for word in corrected_list:
    print(word.correct(),end="")



