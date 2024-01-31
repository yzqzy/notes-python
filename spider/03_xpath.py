from lxml import etree

# # -----------------------------------

"""
lxml 是一款高性能的 Python HTML/XML 解析器，我们可以利用 XPath, 来快速定位特定元素以及获取节点信息.

XPath 是一门在 XML 文档中定位元素的语言，它使用路径表达式来选取节点或者节点集合。
XPath 表达式的语法和一般的表达式类似，但有一些特殊符号用于处理节点和属性。

xpath 语法:
  nodename 选中该元素
  /        从根节点选取、或者是元素和元素间的过渡
  //       从匹配选择的当前节点选择文档中的节点，不考虑它们的位置
  .        选取当前节点
  ..       选取当前节点的父节点
  @        选取属性
  text()   选取元素的文本内容
"""

"""
https://movie.douban.com/top250

选取所有 h1 下的文本
  //h1/text()
获取所有 a 标签的 href
  //a/@href
获取 html 下 head 中 title 的文本
  /html/head/title/text()
获取 html 下 head 中 link 标签的 href
  /html/head/link/@href
"""

"""
查找特定节点

选取 class 属性为 s2 的 span 节点
  //span[@class="s2"]
选取属于 ul 子标签的第一个 li 标签
  //ul/li[1]
"""
