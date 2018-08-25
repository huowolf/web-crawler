'''
Created on 2018年8月22日

@author: huowolf
'''
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp=RobotFileParser()
rp.set_url('https://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.jianshu.com/p/504dd4e96068'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=l&type=collections'))


robot = RobotFileParser()
result = urlopen('http://www.zhihu.com/robots.txt').read().decode('utf-8')
#print(result)

robot.parse(result)

print(robot.can_fetch('*','http://www.zhihu.com/question/29173647/answer/437189494'))#True
print(robot.can_fetch('*','https://www.zhihu.com/signin?next=%2Fexplore'))#True
print(robot.can_fetch('*','http://www.zhihu.com/inbox/7013224000'))#True


