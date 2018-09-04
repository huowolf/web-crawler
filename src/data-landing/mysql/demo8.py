'''
Created on 2018年9月3日

@author: huowolf
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()

sql='select * from students where age>=20'

try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row=cursor.fetchone()
    while row:
        print('Row:',row)
        row=cursor.fetchone()
except Exception as e:
    print('error')
    print(e)
db.close()