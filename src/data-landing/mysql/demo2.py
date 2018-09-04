'''
Created on 2018年9月2日

@author: huowolf
'''
import pymysql

id='20130002'
name='Jack'
age=22
db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()
sql='insert into students(id,name,age) value(%s,%s,%s)'
try:
    cursor.execute(sql,(id,name,age))
    db.commit()
except:
    db.rollback()
db.close()
