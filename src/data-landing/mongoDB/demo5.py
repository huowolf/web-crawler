'''
Created on 2018年9月4日

@author: huowolf
'''
import pymongo

client=pymongo.MongoClient(host='localhost',port=27017)
db=client.test
collection=db.students

condition={'name':'Mary'}
student=collection.find_one(condition)
student['age']=28
result=collection.update(condition,student)
print(result)

student['age']=26
result=collection.update_one(condition,{'$set':student})
print(result.matched_count,result.modified_count)
