'''
Created on 2018年9月16日

@author: huowolf
'''
import time
from selenium import webdriver

browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()
