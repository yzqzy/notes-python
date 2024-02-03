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
    'Cookie': 'buvid4=74A775E0-49D3-6549-21B2-933557E8E51382242-023120614-; buvid3=C9894EE3-1662-60A2-B87E-32F3B093A01624272infoc; b_nut=1701874624; _uuid=67A3F34D-87510-AE6E-1B96-53D9B26412B624817infoc; buvid_fp=a7034611ba2a058e9f4ec4c94e4f1167; DedeUserID=364818348; DedeUserID__ckMd5=ce6f4e4942bfb9ae; CURRENT_FNVAL=4048; bsource=search_google; enable_web_push=DISABLE; header_theme_version=CLOSE; home_feed_column=5; rpdid=|(umYJ)))|~l0J\'u~|u)~lYl); hit-dyn-v2=1; b_lsid=575B1584_18D6D294117; browser_resolution=1440-779; SESSDATA=a2cf4534%2C1722485437%2C68a8a%2A21CjBEB9vmnHslpg-9OoM4nBQHliml5bgT-BVUVjL89j1bSITQd9equb_LFKR5o9U3Z5gSVld1S1NGMEg1YkhkRW9HLXBBTHBUeGFiY3lGbUxZSVJ1Uk9ia1ZnOUlvcDdDM3lxMmVlSGg3QnpsY2NybUlhMVhmbUJ1dG1fSFFHUDFVUU1nWTd2bDR3IIEC; bili_jct=5f9470e6b0bcc479a79638d929744b85; bp_video_offset_364818348=892802419579158529; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDcxOTI3MDIsImlhdCI6MTcwNjkzMzQ0MiwicGx0IjotMX0.Ip7pp0Ky85Xq8BzJOwr3Ndm-urNmzTVYTJsamhIxXg8; bili_ticket_expires=1707192642; sid=79jr7rnc',
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
