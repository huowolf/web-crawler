'''
Created on 2018年8月21日

@author: huowolf
'''
from urllib import request,error

try:
    response=request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
    print('-----------------')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')
