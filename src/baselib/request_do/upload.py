'''
Created on 2018年8月25日

@author: huowolf
'''
import requests

files={'file':open('favicon.ico','rb')}
r=requests.post('http://httpbin.org/post',files=files)
print(r.text)

