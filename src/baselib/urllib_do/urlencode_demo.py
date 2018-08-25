'''
Created on 2018年8月22日

@author: huowolf
'''
from urllib.parse import urlencode, urlparse, parse_qs

params={
    'name':'zhangsan',
    'age':22
}
baseurl='http://baidu.com?'
url=baseurl+urlencode(params)
print(url)

#------------------------------
url='http://baidu.com?name=zhangsan&age=22'
params=urlparse(url).query
print(params)
print(parse_qs(params))
