'''
Created on 2018年9月17日

@author: huowolf
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
 
browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.quit()