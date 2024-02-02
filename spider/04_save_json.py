import requests
import json

from lxml import etree

"""
JSON 文件存储

JSON, 全称为 JavaScript Object Notation, 即 JavaScript 对象标记。
它通过对象和数组的组合来表示数据，构造简单但是结构化程度非常高，是一种轻量级的数据交换格式。
"""

# # -----------------------------------

import requests

url = "https://www.4399.com/flash/"

payload = {}
headers = {}

response = requests.get(url, headers=headers, data=payload)
response.encoding = 'GBK'

html = etree.HTML(response.text)
li_list = html.xpath("//ul[@class='n-game cf']/li")
data_list = []

for li in li_list:
  item = {}
  item['href'] = li.xpath("./a/@href")[0]
  item['title'] = li.xpath("./a/b/text()")[0]
  data_list.append(item)

with open('spider/data_4399_game.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(data_list, ensure_ascii=False, indent=2))

# # -----------------------------------
