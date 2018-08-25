'''
Created on 2018年8月25日

@author: huowolf
'''
import requests

data={
    'name':'zhangsan',
    'age':22
}

r=requests.get('http://httpbin.org/get',params=data)
print(r.text)
print(r.json())
