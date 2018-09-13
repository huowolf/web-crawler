'''
Created on 2018年9月5日

@author: huowolf
'''
from redis import StrictRedis,ConnectionPool

url='redis://:foobared@localhost:6379/0'
pool=ConnectionPool.from_url(url)
redis=StrictRedis(connection_pool=pool)

# result=redis.zadd('grade',100,'Bob',98,'Mike')
# print(result)
# grade=redis.zrange('grade',0,-1)
# print(grade)

# redis.zrem('grade','Mike')

# score=redis.zincrby('grade','Bob',-2)
# print(score)

# redis.zadd('grade',97,'Amy')
# rank=redis.zrank('grade','Amy')
# print(rank)

# revrank=redis.zrevrank('grade','Amy')
# print(revrank)

# grade=redis.zrevrange('grade', 0, -1)
# print(grade)

# grade=redis.zrangebyscore('grade',95,100)
# print(grade)

# count=redis.zcount('grade', 95, 100)
# print(count)

# length=redis.zcard('grade')
# print(length)

# result=redis.zremrangebyrank('grade', 0, 0)
# print(result)

result=redis.zremrangebyscore('grade', 80, 90)
print(result)