'''
Created on 2018年8月30日

@author: huowolf
'''
import csv

with open('data.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike','20'])
    writer.writerow(['10002','Bob','22'])
    writer.writerow(['10003','Jack','21'])