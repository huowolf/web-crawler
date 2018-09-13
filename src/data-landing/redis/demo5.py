'''
Created on 2018年9月6日

@author: huowolf
'''
from redis import StrictRedis,ConnectionPool

url='redis://:foobared@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)

# redis.hset('price', 'cake', 5)
# all=redis.hgetall('price')
# print(all)

# redis.hsetnx('price', 'book', 6)
# all=redis.hgetall('price')
# print(all)

# book=redis.hget('price', 'book')
# print(book)

# values=redis.hmget('price', 'book','cake')
# print(values)

# result=redis.hmset('price', {'banna':2,'pear':6})
# print(result)

# banna=redis.hincrby('price', 'banna', 3)
# print(banna)
# banna=redis.hget('price', 'banna')
# print(banna)

# result=redis.hexists('price', 'banna')
# print(result)

# result=redis.hdel('price','banna')
# print(result)

# keys=redis.hkeys('price')
# print(keys)

# vals=redis.hvals('price')
# print(vals)

items=redis.hgetall('price')
print(items)



