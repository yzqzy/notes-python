from bs4 import BeautifulSoup

"""
和 lxml 一样, BeautifulSoup 也是一个 HTML/XML 解析器。主要的功能也是如何解析和提取 HTML/XML 数据。
lxml 只会局部遍历, BeautifulSoup 是基于 HTML DOM, 会载入整个文档, 解析整个 DOM 树, 因为时间和内存开销都会大很多, 所以性能比 lxml 低。

BeautifulSoup 解析 HTML 比较简单, API 非常人性化, 支持 CSS 选择器, Python 标准库中的 HTML 解析起, 也支持 lxml 的 XML 解析器。

pip install bs4
"""

"""
抓取工具        速度  使用难度  安装难度
正则            慢    复杂      无  
BeautifulSoup  快     简单    简单
lxml           快     简单    一般
"""
