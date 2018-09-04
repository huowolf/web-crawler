'''
Created on 2018年9月2日

@author: huowolf
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()

sql='select * from students where age>=20'

try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    one=cursor.fetchone()
    print('One',one)
    results=cursor.fetchall()
    print('Results',results)
    print('Results Type',type(results))
    for row in results:
        print(row)
except Exception as e:
    print('error')
    print(e)
db.close()

