'''
Created on 2018年8月30日

@author: huowolf
'''
import csv
with open('data2.csv','w') as csvfile:
    fieldnames=['id','name','age']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id':'10001','name':'Mike','age':20})
    writer.writerow({'id':'10002','name':'Bob','age':22})
    writer.writerow({'id':'10003','name':'Jack','age':21})
