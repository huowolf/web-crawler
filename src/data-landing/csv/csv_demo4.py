'''
Created on 2018年8月30日

@author: huowolf
'''
import csv

with open('data.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)
