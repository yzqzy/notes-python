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

Match
  - group() 返回匹配到的字符串
  - start() 返回匹配到的字符串的起始位置
  - end() 返回匹配到的字符串的结束位置
  - span() 返回匹配到的字符串的起始和结束位置

Search
  - group() 返回匹配到的字符串
  - start() 返回匹配到的字符串的起始位置
  - end() 返回匹配到的字符串的结束位置
  - span() 返回匹配到的字符串的起始和结束位置

findall
  - 返回所有匹配到的子串的列表

sub
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


# # -----------------------------------
