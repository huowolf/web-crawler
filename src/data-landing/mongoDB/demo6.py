'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students

condition={'age':{'$gt':20}}
result=collection.update_one(condition,{'$inc':{'age':1}})
print(result.matched_count,result.modified_count)

condition={'age':{'$gt':20}}
result=collection.update_many(condition,{'$inc':{'age':1}})
print(result.matched_count,result.modified_count)