import csv
import requests

"""
表格文件存储

CSV, 全称 Comma Separated Values, 即逗号分隔值文件, 其文件以纯文本形式存储数据。
"""

# # -----------------------------------

"""
数组写入
"""

# with open('spider/data_array_test.csv', 'w') as f:
#   writer = csv.writer(f, delimiter='\t')
#   writer.writerow(['name', 'age', 'gender'])
#   writer.writerow(['Alice', 25, 'female'])
#   writer.writerow(['Bob', 30, 'male'])
#   writer.writerow(['Charlie', 35, 'female'])

# # -----------------------------------

"""
字典写入
"""

# with open('spider/data_dict_test.csv', 'w') as f:
#   writer = csv.DictWriter(f, fieldnames=['name', 'age', 'gender'])
#   writer.writeheader()
#   writer.writerow({'name': 'Alice', 'age': 25, 'gender': 'female'})
#   writer.writerow({'name': 'Bob', 'age': 30, 'gender': 'male'})
#   writer.writerow({'name': 'Charlie', 'age': 35, 'gender': 'female'})

# # -----------------------------------

"""
bilibili 搜索结果写入
"""

url = "https://api.bilibili.com/x/web-interface/wbi/search/type?category_id=&search_type=media_bangumi&ad_resource=5646&__refresh__=true&_extra=&context=&page=1&page_size=12&order=&duration=&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E5%A5%A5%E7%89%B9%E6%9B%BC&qv_id=3qrdY8g9wzV5ONnpw900c3bOYaFXO4kL&source_tag=3&gaia_vtoken=&web_location=1430654&w_rid=ad6ecd55b037fdef134d63cc6cb90646&wts=1706945950"
headers = {
    'Cookie': 'your cookie',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

with open('spider/data_bilibili_search.csv', 'w') as f:
  fileds = ['标题', '链接', '产地']
  writer = csv.DictWriter(f, fieldnames=fileds)
  writer.writeheader()
  for res in response.json()['data']['result']:
    writer.writerow({'标题': res['title'], '链接': res['url'], '产地': res['areas']})

# # -----------------------------------
