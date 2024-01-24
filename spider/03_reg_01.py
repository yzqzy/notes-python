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
print(json_str, type(json_str))  # {"name": "heora", "age": 28} <class 'str'>

json_obj = json.loads(json_str)  # 将 json 字符串转换为 python 对象
print(json_obj, type(json_obj))  # {'name': 'heora', 'age': 28} <class 'dict'>


# # -----------------------------------

"""
正则表达式

用事先定义的一些特定字符及特定字符的组合，组成一个 “规则字符”，这个规则字符串用来表达对字符串的一种过滤逻辑。
"""

# # -----------------------------------
