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
sql='insert into {table}({keys}) values ({values}) on duplicate key update'.format(table=table,keys=keys,values=values)
update=','.join(' {key}=%s'.format(key=key) for key in data)
sql+=update
print(sql)
try:
    cursor.execute(sql,tuple(data.values())*2)
    db.commit()
    print('successful')
except:
    print('Field')
    db.rollback()
db.close()
