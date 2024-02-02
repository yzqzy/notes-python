import requests

from bs4 import BeautifulSoup

"""
文件打开模式

r:    只读方式打开文件、文件的指针会放在文件开头（默认模式）
rb:   二进制只读方式打开一个文件，文件指针会放在文件开头
r+:   读写方式打开文件，文件指针会放在文件开头
rb+:  二进制读写方式打开一个文件，文件指针会放在文件开头
w:    写入方式打开文件，文件指针会放在文件开头并清空原有内容
wb:   二进制写入方式打开一个文件，文件指针会放在文件开头并清空原有内容
w+:   读写方式打开文件，文件指针会放在文件开头并清空原有内容
wb+:  二进制读写方式打开一个文件，文件指针会放在文件开头并清空原有内容
a:    追加方式打开文件，文件指针会放在文件结尾
ab:   二进制追加方式打开一个文件，文件指针会放在文件结尾
a+:   读写追加方式打开文件，文件指针会放在文件结尾
ab+:  二进制读写追加方式打开一个文件，文件指针会放在文件结尾
"""

"""
文本存储

txt 文本操作很简单，几乎兼容所有平台，但是不利于检索
"""

# # -----------------------------------

url = 'https://www.zhihu.com/explore'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
title_list = soup.select('div.css-1g4zjtl > a')

for title in title_list:
  print(title.get_text())
  with open('spider/data_zhihu_explore.txt', 'a', encoding='utf-8') as f:
    f.write(title.get_text() + '\n')

# # -----------------------------------
