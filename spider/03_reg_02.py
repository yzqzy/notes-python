import re

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
print(ret.group())  # hello@163.com
print(ret.group(1))  # 163

# # -----------------------------------
