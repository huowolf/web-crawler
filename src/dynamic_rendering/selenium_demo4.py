'''
Created on 2018年9月16日

@author: huowolf
'''
from selenium import webdriver
import time
 
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name('btn-search')
button.click()