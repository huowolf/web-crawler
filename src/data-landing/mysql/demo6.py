'''
Created on 2018年9月2日

@author: huowolf
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()

table='students'
condition='age>20'
sql='delete from {table} where {condition}'.format(table=table,condition=condition)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
