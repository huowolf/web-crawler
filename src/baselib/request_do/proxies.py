'''
Created on 2018年8月25日

@author: huowolf
'''
import requests

proxies = {
  "http": "http://167.99.156.71:8080",
}

r=requests.get("http://www.baidu.com", proxies=proxies)
print(r.status_code)