'''
Created on 2018年9月5日

@author: huowolf
'''
from redis import StrictRedis,ConnectionPool

url='redis://:foobared@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)

# redis.sadd('tags','Book','Tea','Coffee')
# set=redis.smembers('tags')
# print(set)

# redis.srem('tags','Book')

# item=redis.spop('tags')
# print(item)

# result=redis.smove('tags', 'tags2', 'Coffee')
# print(result)
# set=redis.smembers('tags')
# print(set)
# set2=redis.smembers('tags2')
# print(set2)

# length=redis.scard('tags')
# print(length)

# result=redis.sismember('tags', 'Book')
# print(result)

# inter=redis.sinter(['tags','tags2'])
# print(inter)

# redis.sinterstore('intertag', ['tags','tags2'])
# intertag=redis.smembers('intertag')
# print(intertag)

# union=redis.sunion(['tags','tags2'])
# print(union)

# redis.sunionstore('uniontag', ['tags','tags2'])
# uniontag=redis.smembers('uniontag')
# print(uniontag)

# diff=redis.sdiff(['tags','tags2'])
# print(diff)

# redis.sdiffstore('difftag', ['tags','tags2'])
# difftag=redis.smembers('difftag')
# print(difftag)

item=redis.srandmember('tags')
print(item)





