'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students
student1={
    'id':'2014001',
    'name':'Jack',
    'age':20,
    'gender':'male'
}
student2={
    'id':'2014002',
    'name':'Mary',
    'age':22,
    'gender':'Female'
}
result=collection.insert_many([student1,student2])
print(result.inserted_ids)
