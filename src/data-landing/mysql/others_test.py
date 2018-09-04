'''
Created on 2018年9月2日

@author: huowolf
'''
data={
    'id':'2013001',
    'name':'bob',
    'age':20
}
print(len(data))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print(type(data.values()))
print(data.values())
print(tuple(data.values()))