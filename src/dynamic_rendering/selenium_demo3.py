'''
Created on 2018年9月16日

@author: huowolf
'''
from selenium import webdriver

browser = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
browser.get('https://www.taobao.com')
input_first=browser.find_element_by_id('q')
input_second=browser.find_elements_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()
