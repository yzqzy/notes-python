import re
import requests

# # -----------------------------------

"""
匹配分组

|         匹配左右任意一个表达式
(ab)      将括号中字符作为一个分组
\num      引用分组 num 匹配到的字符串
(?p)      分组起别名
(?P=name) 引用别名为name分组匹配到的字符串
"""

# 需求：在列表 ['apple', 'banana', 'orange', 'pear'] 中匹配 apple 和 pear
# fruits = ['apple', 'banana', 'orange', 'pear']
# for fruit in fruits:
#   ret = re.match(r'apple|pear', fruit)
#   if ret:
#     print(f'fruit {ret.group()}')

# 需求: 匹配出 163,126,qq 等邮箱
ret = re.match('[a-zA-Z0-9_]{4,20}@(163|11|qq)\.com', 'hello@163.com')
# print(ret.group())  # hello@163.com
# print(ret.group(1))  # 163

"""
*    匹配0个或多个字符
+    匹配1个或多个字符
?    匹配0个或1个字符
{n}  匹配n个字符
{n,} 匹配n个或多个字符
{n,m} 匹配n-m个字符
"""

# \num
# str = '<html>hh</html>'
# ret = re.match('<[A-Za-z1-6]+>.*</[A-Za-z1-6]+>', str)
# print(ret.group())  # <html>hh</html>
# ret = re.match('<[A-Za-z1-6]+>(.*)</[A-Za-z1-6]+>', str)
# print(ret.group(1))  # hh
# ret = re.match('<([A-Za-z1-6]+)>.*</\\1>', str)  # \num 代表取出前面匹配规则，这里是[A-Za-z1-6]+
# print(ret.group(1))  # html

# (?p) (?p=name)

# str = '<html><h1>www.yueluo.club</h1></html>'
# ret = re.match('<[A-Za-z1-6]+><[A-Za-z1-6]+>.*</[A-Za-z1-6]+></[A-Za-z1-6]+>', str)
# print(ret.group())  # <html><h1>www.yueluo.club</h1></html>
# ret = re.match('<([A-Za-z1-6]+)><([A-Za-z1-6]+)>.*</\\2></\\1>', str)
# print(ret.group())  # <html><h1>www.yueluo.club</h1></html>
# ret = re.match('<(?P<name1>[A-Za-z1-6]+)><(?P<name2>[A-Za-z1-6]+)>.*</(?P=name2)></(?P=name1)>', str)
# print(ret.group())  # <html><h1>www.yueluo.club</h1></html>

# # -----------------------------------

"""
r 方式数据进行转译

原始字符串定义(raw string)：所有的字符串都是直接按照字面的意思来使用，没有转移特殊或不能打印的字符，
原始字符串往往针对特殊字符而言，例如 "\n" 的原始字符串就是 "\\n"。

正则中使用原始字符串的语法是 r"..."，例如 r"\n" 匹配 "\n" 而不是换行符。
在 Python 中，原始字符串的语法是以 r 开头，后面紧跟字符串内容，例如 r"hello\nworld"。
在 Python 中，原始字符串的作用是为了防止转义字符的影响，例如 r"hello\nworld" 实际上是 "hello\nworld"，
而不是 "hello" 和 "world" 之间换行。

wndows 中在路径的时候可以添加，可以自动转换路径
"""

# # -----------------------------------

"""
匹配中文
"""

title = "你好, hello, 世界"

# ret = re.findall('[\u4e00-\u9fa5]+', title)
# print(ret)  # ['你好', '世界']


# # -----------------------------------

"""
贪婪、非贪婪

贪婪匹配：正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配（默认是贪婪匹配）
非贪婪匹配：匹配到结果就好，就少的匹配字符，在量词后面直接加上一个问号?，就是非贪婪模式
"""

# ret = re.match('[A-Z][a-z]*', 'Aadakjaldjasljdlasjdlasdalda')
# print(ret.group())  # Aadakjaldjasljdlasjdlasdalda
# ret = re.match('[A-Z][a-z]*?', 'Aadakjaldjasljdlasjdlasdalda')
# print(ret.group())  # A

# # -----------------------------------

"""
实际案例
"""

url = 'https://www.dns.com/'
response = requests.get(url)
data = re.findall('var web2LoginUrl = \'(.*?)\';', response.text)
print(data)  # ['https://www.dns.com/login.html']

# # -----------------------------------
