from urllib.parse import urlparse, urlunparse

result=urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
print(result.netloc)
print(result[1])

data=['http','www.baidu.com','/index.html','user','id=5','comment']
print(urlunparse(data))