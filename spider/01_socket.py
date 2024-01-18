import re
import socket

url = 'http://pic.bizhi360.com/bbpic/98/10798.jpg'

"""
http/1.0 
  connection: keep-alive 默认不启动
http/1.1
  1. 默认启动 keep-alive
  2. 如果不想使用，可以设置 connection: close
"""

# 1. 创建 socket 套接字
client = socket.socket()

# 2. 创建连接
client.connect(('pic.bizhi360.com', 80))

# 3. 构造 http 请求
http_req = 'GET ' + url + ' HTTP/1.0\r\n' + \
    'Host: pic.bizhi360.com\r\n' + \
    'Upgrade-Insecure-Requests: 1\r\n' + \
    'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1\r\n' + \
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n' + \
    '\r\n'

# 4. 发送 http 请求
client.send(http_req.encode())

result = b''

# 5. 接收数据信息
data = client.recv(1024)

while data:
  result += data
  data = client.recv(1024)

# print(result)

# 6. 提取响应体数据
content = re.findall(b'\r\n\r\n(.*)', result, re.S)
# print(content[0])

# 7. 保存数据到本地
with open('spider/imgs/test.png', 'wb') as f:
  f.write(content[0])
