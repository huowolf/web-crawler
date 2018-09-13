'''
Created on 2018年9月12日

@author: huowolf
'''
import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
from re import RegexFlag
import re
import os
from hashlib import md5
from multiprocessing.pool import Pool
import pymongo

GROUP_START=1
GROUP_END=10
keyword='街拍'
save_dir='d:\imges'

MONGO_HOST='localhost'
MONGO_DB='toutiao'
MONGO_TABLE='toutiao'


client=pymongo.MongoClient(MONGO_HOST)
db=client[MONGO_DB]

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print ('存储到MongoDB成功！',result)
        return True
    return False

def get_page_index(offest,keyword):
    params={
        'offest':offest,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab'
    }
    
    url='https://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        else:
            return None
    except RequestException:
        print('请求索引页错误')
        return None
        
# 分析ajax请求的返回结果，获取图片集的url
def parse_page_index(html):
    data = json.loads(html) # 加载返回的json数据
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
            
            
# 获取详情页的内容
def get_page_detail(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print('请求详情页错误', url)
        return None            
            
#获取网页图集名及图片网址
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml') #声明BeautifulSoup的lxml对象
    title = soup.select('title')
    if title:
        title = title[0].get_text()

    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)',RegexFlag.S)
    result = re.search(images_pattern,html)
    if result:
        result = result.group(1).replace('\\','')
        data = json.loads(result)
        if data and 'sub_images'in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                #下载图片             
                download_image(image,save_dir)
            return { #数据格式化返回，方便后续操作
                'title':title,
                'url':url,
                'images':images
            }

#请求下载图片
def download_image(url,save_dir):
    print("正在下载",url)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            save_image(response.content,save_dir) #content返回二进制结果，text返回网页正常结果
        return None
    except RequestException:
        print("请求图片出错")
        return None
    
#下载图片
def save_image(content,save_dir):
    if not os.path.exists(save_dir): #如果文件夹不存在创建文件夹
        os.mkdir(save_dir)
    # 第一个参数是保持路径，第二个参数用来去掉重复图片，第三个参数为图片的格式
    file_path = '{0}/{1}.{2}'.format(save_dir,md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,"wb") as f:
            f.write(content)
            f.close()
            
def main(offset):
    html = get_page_index(offset,keyword)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            #print(result)
            save_to_mongo(result)


if __name__ == '__main__':
    groups = [x*20 for x in range(GROUP_START,GROUP_END)]
    pool = Pool() #声明多线程Pool对象
    pool.map(main,groups) #多线程map函数实现多线程
    pool.close()
    pool.join()

