'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students

result=collection.delete_one({'name':'Jack'})
print(result.deleted_count)
result=collection.delete_many({'age':{'$gt':25}})
print(result.deleted_count)