'''
Created on 2018年8月25日

@author: huowolf
'''
import requests
import urllib3

urllib3.disable_warnings()
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
