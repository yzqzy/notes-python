import requests

# # -----------------------------------

"""
response
  text  响应体 str 类型
    request 模块自动根据 HTTP 头部对响应的编码作出有根据的推荐
    修改编码方式: response.encoding = 'utf-8'

  content 响应体 bytes 类型
    类型: bytes
    修改编码方式: response.content.decode('utf-8')

  json  响应体 json 数据

  request.headers 请求头

  status_code 状态码
  headers 响应头
  cookies 经过 set-cookie 动作
"""

url = 'https://www.baidu.com'

# response = requests.get(url)

# response.encoding = 'utf-8'

# print(response.text)
# print(response.content.decode('utf-8'))

# print(response.status_code)
# print(response.request.headers)
# print(response.cookies)

# # -----------------------------------

"""
下载百度图标
"""

url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'

# response = requests.get(url)

# with open('spider/imgs/baidu.png', 'wb') as f:
#   f.write(response.content)

# # -----------------------------------

"""
模拟 headers 请求
"""

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

# response = requests.get(url, headers=headers)

# print(response.content.decode('utf-8'))
# print(response.request.headers)

# # -----------------------------------

"""
带参数请求
"""


# url = 'https://www.baidu.com?wd=python'
# response = requests.get(url)

url = 'https://www.baidu.com/s'

head = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}
kw = {
    'wd': 'python'
}

# response = requests.get(url, params=kw, headers=head)

# print(response.content.decode('utf-8'))

# # -----------------------------------

"""
post 请求

1. POST 比 GET 更加安全，因为 GET 请求参数在 URL 中，容易被浏览器缓存，而 POST 请求参数在请求体中，不会被缓存。
2. POST 请求可以上传大量数据，而 GET 请求的 URL 长度有限制。
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data = {
    'column': 'szse_latest',
    'pageNum': '1',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}

url = 'http://www.cninfo.com.cn/new/disclosure'

# response = requests.post(url, headers=headers, data=data)

# print(response.text)
# print(response.json())

# # -----------------------------------

"""
proxy

"""

proxies = {
    'http': 'http://110.12.211.140:80',
}

url = 'http://httpbin.org/ip'
response = requests.get(url, proxies=proxies)

print(response.text)

# # -----------------------------------
