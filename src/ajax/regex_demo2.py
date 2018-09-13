'''
Created on 2018年9月12日

@author: huowolf
'''
import re
s = "abc(hello)casdf"
#[ ]具有去特殊符号的作用,也就是说[(]里的(只是平凡的括号
text=re.findall(r'[^()]+', s)[1]
print(text)

m = re.match(".*\((.*)\).*", s)
print(m.group(1))
