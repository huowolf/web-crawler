'''
Created on 2018年9月2日

@author: huowolf
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()
sql='''CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, 
age INT NOT NULL,PRIMARY KEY (id ))'''
cursor.execute(sql)
db.close()