'''
Created on 2018年9月5日

@author: huowolf
'''
from redis import StrictRedis,ConnectionPool

url='redis://:foobared@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)

# redis.set('name','Bob')
# name=redis.get('name')
# print(name)

# oldname=redis.getset('name','Mike')
# print(oldname)

# redis.set('nickname','Miker')
# name_list=redis.mget(['name','nickname'])
# print(name_list)

# result=redis.setnx('newname','James')
# print(result)

#redis.setex('name', 10, 'James')

# redis.set('name','Hello')
# length=redis.setrange('name', 6, 'World')
# print(length)

# redis.mset({'name1':'Jack','name2':'Mary'})

# result=redis.msetnx({'name3':'Smith','name4':'Curry'})
# print(result)

# age=redis.incr('age',1)
# print(age)

# age=redis.decr('age',1)
# print(age)

# redis.append('nickname', 'OK')
# nickname=redis.get('nickname')
# print(nickname)

# substr=redis.substr('name', 1, 4)
# print(substr)

substr=redis.getrange('name', 1, 4)
print(substr)

