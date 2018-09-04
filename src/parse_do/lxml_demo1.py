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

#获取所有li 节点下所有a 节点的href 属性
result=html.xpath('//li/a/@href')
print(result)

#多值属性匹配
text='''
<li class='li li-first'><a href="link1.html">first item</a></li>
'''
html=etree.HTML(text)
result=html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

#多属性匹配 and
text = '''
<li class="li li-first" name="item"><a href="https://ask.hellobi.com/link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

#按序选择
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
#选取第一个 li 节点
result = html.xpath('//li[1]/a/text()')
print(result)
#选取最后一个 li 节点
result = html.xpath('//li[last()]/a/text()')
print(result)
#选取前 2个 li 节点
result = html.xpath('//li[position()<3]/a/text()')
print(result)
#选取倒数第三个 li 节点
result = html.xpath('//li[last()-2]/a/text()')
print(result)


#节点轴选择
#轴可定义相对于当前节点的节点集

#第一个 li 节点的所有祖先节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
#选取第一个 li 节点的div 这个祖先节点
result = html.xpath('//li[1]/ancestor::div')
print(result)
#第一个 li 节点的所有属性值
result = html.xpath('//li[1]/attribute::*')
#第一个 li 节点的所有直接子节点中的 href 属性为 link1.html 的 a 节点
result = html.xpath('//li[1]/child::a[@href="https://ask.hellobi.com/link1.html"]')
print(result)
#descendant:选取当前节点的所有后代元素（子、孙等）。
result = html.xpath('//li[1]/descendant::span/text()')
print(result)
#following：选取文档中当前节点的结束标签之后的所有节点。
result = html.xpath('//li[1]/following::*[2]/text()')
print(result)
#following-sibling：选取当前节点之前的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)
