'''
Created on 2018年9月16日

@author: huowolf
'''
import time
from selenium import webdriver

browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://news.qq.com/')

