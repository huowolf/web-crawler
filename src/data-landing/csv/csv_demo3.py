'''
Created on 2018年8月30日

@author: huowolf
'''
import csv

with open('data.csv','a',encoding='utf-8',newline='') as csvfile:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writerow({'id':'10004','name':'小明','age':25})
