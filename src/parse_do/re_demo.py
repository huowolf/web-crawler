'''
Created on 2018年8月25日

@author: huowolf
'''
import re

#非贪婪匹配
context='Hello 1234567 World_This is a Regex Demo'
result=re.match('^He.*?(\d+).*Demo$',context)
print(result.group(1))

#sub
context='54xyz67werzz89'
context=re.sub('\d+','',context)
print(context)

#修饰符
#.（点）可以匹配任意字符（除换行符）
#re.S:使.匹配包括换行符在内的所有字符
content = '''Hello 1234567 World_This
is a Regex Demo
'''
#result = re.match('^He.*?(\d+).*?Demo$', content,re.S)
print(result.group(1))
