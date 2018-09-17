'''
Created on 2018年9月16日

@author: huowolf
'''
from selenium import webdriver

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('--headless')
#option.add_argument('disable-infobars')
chromedriver_path=r'D:\chromedriver\chromedriver.exe'

# 打开chrome浏览器
driver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=option)
driver.get("https://www.baidu.com") 

# 打印页面标题 "百度一下，你就知道"
print(driver.title)

# 生成当前页面快照并保存
driver.save_screenshot("baidu.png")

# 关闭浏览器
driver.quit()

