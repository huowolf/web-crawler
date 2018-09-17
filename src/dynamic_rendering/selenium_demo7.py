'''
Created on 2018年9月16日

@author: huowolf
'''
from selenium import webdriver
 
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)