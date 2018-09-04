'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
student={
    'id':'2013001',
    'name':'zhangsan',
    'age':20,
    'gender':'male'
}
#result=collection.insert(student)
#print(result)


student={
    'id':'2013002',
    'name':'lisi',
    'age':22,
    'gender':'male'
}
result=collection.insert_one(student)
print(result)
print(result.inserted_id)