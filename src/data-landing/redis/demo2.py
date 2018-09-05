'''
Created on 2018年9月5日

@author: huowolf
'''
from redis import StrictRedis,ConnectionPool

url='redis://:foobared@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)

# length=redis.rpush('list',1,2,3)
# print(length)

# redis.lpush('list',0)
# list=redis.lrange('list', 0, -1)
# print(list)

# length=redis.llen('list')
# print(length)

# redis.ltrim('list', 1, 3)
# list=redis.lrange('list', 0, -1)
# print(list)

# item=redis.lindex('list', 1)
# print(item)

# result=redis.lset('list',1,5)
# print(result)

# redis.lrem('list',2,3)

# item=redis.lpop('list')
# print(item)

# item=redis.rpop('list')
# print(item)

redis.rpoplpush('list', 'list2')
list=redis.lrange('list', 0, -1)
print(list)
list2=redis.lrange('list2', 0, -1)
print(list2)

