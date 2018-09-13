'''
Created on 2018年9月12日

@author: huowolf
'''
import requests
import re
from re import RegexFlag
url='https://www.toutiao.com/a6575128377458426371/'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
}
response=requests.get(url,headers=headers)
if response.status_code==200:
    print('successful')
html=response.text
print('-----------------------------------')
image_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)',RegexFlag.S)
#image_pattern = re.compile('gallery: JSON.parse[(]"(.*?)"[)],\n',re.S)
result = re.search(image_pattern,html)
if result:
    result = result.group(1).replace('\\','')
    #print(result.group(1))
    print(result)

