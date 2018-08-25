'''
Created on 2018年8月25日

@author: huowolf
'''
from lxml import etree

text = '''
<div>
<Ul>
<li class="item-O"><a href="linkl. html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class＝"item-O"><a href＝"link5.html">fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)
result=etree.tostring(html).decode('utf-8')
print(result)

html=etree.parse('test.html',etree.HTMLParser())
#获取所有li节点
result=html.xpath('//li')
print(result)
print(result[0])

#获取所有li 节点的所有直接a 子节点
result=html.xpath('//li/a')
print(result)

#先选中href 属性为link4.html 的a 节点，然后再获取其父节点，然后再获取其class属性
result=html.xpath('//a[@href ="link4.html"]/../@ class')
print(result)

#选取class 为item-O 的li节点
result=html.xpath('//li[@class="item-O"]')
print(result)

#选取class 为item-O 的li节点内的文本
result=html.xpath('//li[@class="item-O"]/a/text()')
print(result)

result=html.xpath('//li[@class="item-O"]//text()')
print(result)
