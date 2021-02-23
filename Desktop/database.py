from sqlalchemy import create_engine
import pandas as pd
import pymysql
sqlEngine= create_engine('mysql+pymysql://root:@127.0.0.1/django')

#sqlEngine = create_engine("mysql+pymysql://{userid}:{password}@localhost/{database}".format(userid="root",password="",database="scores"))
dbConnect= sqlEngine.connect()
try:
    query="insert into books values(Null,'{0}','{1}','{2}')".format()
    n=sqlEngine.execute("insert into values('bookname','bookid','price')")
    if n:
        print("Record Inserted")
except: 
    print("Error")
result=sqlEngine.execute("select * from `siteusers` ")
print(result)
for item in result: 
    print("\nRecord\n")
    for key in result.keys():
        print(key,item[key],end=" , ")
        
