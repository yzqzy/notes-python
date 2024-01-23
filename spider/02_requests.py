import requests

from retrying import retry

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

可以用这个网址测试代理是否成功，如果代理有问题就不使用这个代理地址。
"""

proxies = {
    'http': 'http://110.12.211.140:80',
}

# url = 'http://httpbin.org/ip'
# response = requests.get(url, proxies=proxies)

# print(response.text)

# # -----------------------------------

"""
处理 cookie

1. cookie 字符串放在 headers 中
2. cookie 字典传给请求方法的 cookies 参数接收
3. 使用 requests 提供的 session 模块
"""

url = 'http://www.cninfo.com.cn/new/disclosure'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Cookie': 'JSESSIONID=F0318ECF99317377DECBAB9ABDBE4179; SF_cookie_4=17470996; insert_cookie=45380249; routeId=.uc1; _sp_ses.2141=*; _sp_id.2141=73ef8a62-1c03-4e40-b5d8-b2b30148e70e.1705832961.2.1705964771.1705833595.fd0a2368-dd81-43db-814d-ad0296defc4b'
}
data = {
    'column': 'szse_latest',
    'pageNum': '1',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}

# response = requests.post(url, headers=headers, data=data)
# print(response.json())

# sesstion 处理 cookie, 会话保持
session = requests.session()

url = 'http://www.cninfo.com.cn/new/commonUrl?url=disclosure/list/notice#szse'

response = session.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
})
# print(response.cookies)

url = 'http://www.cninfo.com.cn/new/disclosure'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}
data = {
    'column': 'szse_latest',
    'pageNum': '1',
    'pageSize': '30',
    'sortName': '',
    'sortType': '',
    'clusterFlag': 'true'
}
response = session.post(url, headers=headers, data=data)
# print(response.request.headers)

# # -----------------------------------

"""
cookieJar
"""

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)
print(response.cookies.get_dict())
print(cookies == response.cookies.get_dict())  # True

# # -----------------------------------

"""
忽略证书错误
"""

# response = requests.get('https://www.12306.cn', verify=False)

# # -----------------------------------


"""
超时参数使用

这个方法也可以用来检测代理IP质量，如果一个代理IP很长时间没有响应，添加超时后会报错，可以删除这个IP
"""

# response = requests.get('https://www.baidu.com', timeout=2)

# # -----------------------------------

"""
retrying 模块

使用超时参数可以加快整体请求速度，但是在正常的网页浏览过程中，还会存在速度很慢的情况，这时我们可以选择刷新页面。

pip install retrying

1. retrying 模块是用来处理网络请求失败的，可以自动重试，直到成功为止。
2. 通过装饰器的方式使用，可以让被装饰的函数反复执行
3. retry 中可以传入参数 stop_max_attempt_number 用来设置最大重试次数，默认是3次。
4. retry 中可以传入参数 wait_fixed 用来设置每次重试的间隔时间，默认是1000ms。
5. retry 中可以传入参数 retry_on_exception 用来设置是否重试异常，默认是True。
"""


@retry(stop_max_attempt_number=3, wait_fixed=1000)
def get_baidu():
  response = requests.get('https://www.baidu.com', timeout=2)
  if response.status_code != 200:
    raise Exception('请求失败')
  return response.text


print(get_baidu())

# # -----------------------------------
