'''
Created on 2018年8月25日

@author: huowolf
'''
import requests

r=requests.get('https://github.com/favicon.ico')
with open('favicon.ico','wb') as f:
    f.write(r.content)
