'''
Created on 2018年9月16日

@author: huowolf
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
 
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
browser.close()