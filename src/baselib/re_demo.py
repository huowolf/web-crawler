'''
Created on 2018年8月25日

@author: huowolf
'''
import re

#非贪婪匹配
context='Hello 1234567 World_This is a Regex Demo'
result=re.match('^He.*?(\d+).*Demo$',context)
print(result.group(1))
