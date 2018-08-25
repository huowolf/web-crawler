'''
Created on 2018年8月25日

@author: huowolf
'''
import requests

def get_one_page(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }  
    respons=requests.get(url,headers=headers)
    if respons.status_code==200:
        return respons.text
    return None

def main():
    url='http://maoyan.com/board/4'
    html=get_one_page(url)
    print(html)
    
main()


