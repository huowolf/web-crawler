'''
Created on 2018年9月2日

@author: huowolf
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()
sql='update students set age=%s where name=%s'
try:
    cursor.execute(sql,(25,'bob'))
    db.commit()
except:
    db.rollback()
db.close()