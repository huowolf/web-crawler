'''
Created on 2018年8月22日

@author: huowolf
'''
from urllib.parse import quote, unquote

keyword='壁纸'
url='http://www.baidu.com?wd='+quote(keyword)
print(url)

#----------------------------------------
url='http://www.baidu.com?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
