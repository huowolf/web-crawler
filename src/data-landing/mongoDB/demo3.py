'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students

result=collection.find_one({'name':'Jack'})
print(type(result))
print(result)

print('*'*20)
results=collection.find({'age':20})
print(results)
for result in results:
    print(result)

print('*'*20)
results=collection.find({'age':{'$gt':20}})
print(results)
for result in results:
    print(result)
