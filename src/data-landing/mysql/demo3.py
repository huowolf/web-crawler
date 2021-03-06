'''
Created on 2018年9月2日

@author: huowolf
'''
import pymysql

data={
    'id':'2013001',
    'name':'bob',
    'age':20
}
table='students'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))

db=pymysql.connect(host='localhost',user='root',password='root',db='spiders')
cursor=db.cursor()
sql='insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
print(sql)
try:
    cursor.execute(sql,tuple(data.values()))
    db.commit()
except:
    db.rollback()
db.close()
