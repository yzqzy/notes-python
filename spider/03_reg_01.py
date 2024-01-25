import re
import json

# # -----------------------------------

"""
爬虫分类

结构化数据: json、xml 等
  直接方式：直接转换为 python 类型
非结构化数据: HTML
  处理方式: 正则表达式、xpath、bs4 等
"""

# # -----------------------------------

"""
结构化数据

ensure_ascii=False  # 禁用 ascii 编码, 输出中文字符
"""

json_obj = {"name": "heora", "age": 28}

json_str = json.dumps(json_obj)  # 将 python 对象转换为 json 字符串
# print(json_str, type(json_str))  # {"name": "heora", "age": 28} <class 'str'>

json_obj = json.loads(json_str)  # 将 json 字符串转换为 python 对象
# print(json_obj, type(json_obj))  # {'name': 'heora', 'age': 28} <class 'dict'>


# # -----------------------------------

"""
正则表达式

用事先定义的一些特定字符及特定字符的组合，组成一个 “规则字符”，这个规则字符串用来表达对字符串的一种过滤逻辑。

re 模块: 
  - match 匹配操作，从头开始匹配
  - search 匹配操作，从任意位置开始匹配
  - findall 匹配所有符合规则的子串
  - sub 替换操作，将符合规则的子串替换为其他字符串

Match 匹配一个
  - group() 返回匹配到的字符串
  - start() 返回匹配到的字符串的起始位置
  - end() 返回匹配到的字符串的结束位置
  - span() 返回匹配到的字符串的起始和结束位置

Search 匹配一个
  - group() 返回匹配到的字符串
  - start() 返回匹配到的字符串的起始位置
  - end() 返回匹配到的字符串的结束位置
  - span() 返回匹配到的字符串的起始和结束位置

findall 匹配多个
  - 返回所有匹配到的子串的列表

sub 替换
  - 将所有匹配到的子串替换为其他字符串
"""

result = re.match("heora", "heora is a good man")
info = result.group()
# print(info)  # heora

# # -----------------------------------

"""
匹配单个字符

. 匹配任意1一个字符, 除了\n

[] 匹配[]中列举的字符中的任意1个字符
[^] 匹配[]中列举的字符以外的任意1个字符
\ 转义字符, 用于匹配[]中列举的字符中的特殊字符

\d 匹配任意1个数字, 0-9
\D 匹配任意1个非数字, 除了0-9
\s 匹配任意1个空白字符, 包括空格、制表符、换行符等
\S 匹配任意1个非空白字符
\w 匹配任意1个字母、数字、下划线
\W 匹配任意1个非字母、数字、下划线
"""

result = re.match('.', 'M')
# print(result.group())  # M

result = re.match('.', '\nM')
# 匹配不成功会报错
# print(result.group())

result = re.match('M.', 'MM')
# print(result.group())  # MM

str1 = 'hello'
str2 = 'Hello'
result1 = re.match('[hH]ello', str1)
result2 = re.match('[hH]ello', str2)
# print(result1.group(), result2.group())  # hello Hello

str = '1hello'
result = re.match('[0123456789]hello', str)
# print(result.group())  # 1hello

# ret = re.match('长江\d号', '长江7号')
# print(ret.group())  # 长江7号

# ret = re.match('\D', '长江7号')
# print(ret.group())  # 长

# ret = re.match('\D', '长江7号')
# print(ret.group())  # 长

# ret = re.match('hello\sworld', 'hello world')
# print(ret.group())  # hello world

# ret = re.match('hello\Sworld', 'helloYworld')
# print(ret.group())  # helloYworld

ret = re.match('hello\wworld', 'helloAworld')
# print(ret.group())  # helloAworld

# # -----------------------------------

"""
findall
  
返回所有匹配到的子串的列表
"""

res = re.findall('\d', 'tu12adas32')
# print(res)  # ['1', '2', '3', '2']

"""
sub
"""

res = re.sub('\d', '_', 'tu12adas32')
# print(res)  # tu__adas__

# # -----------------------------------

"""
compile

修饰符
- re.l 使匹配对大小写不敏感
- re.L 使匹配对大小写敏感
- re.M 使 ^ 和 $ 匹配字符串的开头和结尾，即使它们出现在字符串的中间，多行匹配
- re.S 使 . 匹配包括换行符在内的所有字符
- re.U 使 \w, \W, \b, \B, \d, \D, \s, \S 匹配 Unicode 字符
- re.X 使正则表达式可以用更加灵活的语法

将正则表达式编译成 Pattern 对象, 加快匹配速度
"""

p = re.compile('\d', re.S)
res = p.findall('tu12adas32')
# print(res)  # ['1', '2', '3', '2']

# # -----------------------------------

"""
匹配多个字符

*    匹配0个或多个字符
+    匹配1个或多个字符
?    匹配0个或1个字符
{n}  匹配n个字符
{n,} 匹配n个或多个字符
{n,m} 匹配n-m个字符
"""

# * 匹配0个或多个字符
# 需求：匹配出第一个字母为大写字符、后面都是小写字母并且小写字母可有可无
ret = re.match('[A-Z][a-z]*', 'Hellodsada')
# print(ret.group())  # Hellodsada

# + 匹配1个或多个字符
# 需求：匹配一个字符串，第一个字符是t，最一个字符是o，之间至少有一个字符
# ret = re.match('t.+o', 'to')
# ret = re.match('t.+o', 'too')
# print(ret.group())  # too

# ? 匹配0个或1个字符


# # -----------------------------------
