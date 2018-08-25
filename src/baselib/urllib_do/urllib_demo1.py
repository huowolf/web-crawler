'''
Created on 2018年8月21日

@author: huowolf
'''
from urllib import request,parse

url='http://httpbin.org/post'
headers={
    'User-Agent':' Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'Host':'httpbin.org'
}
dict={
    'name':'huowolf'
}
data=bytes(parse.urlencode(dict),encoding='utf8')
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf8'))
