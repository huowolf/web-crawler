'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students

count=collection.find().count()
print(count)

count=collection.find({'age':20}).count()
print(count)

results=collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])

results=collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results=collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])