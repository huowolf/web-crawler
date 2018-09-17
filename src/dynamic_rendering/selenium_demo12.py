'''
Created on 2018年9月16日

@author: huowolf
'''
from selenium import webdriver
 
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
