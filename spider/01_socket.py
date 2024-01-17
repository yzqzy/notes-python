import socket

url = 'http://pic.bizhi360.com/bbpic/98/10798.jpg'

# 创建 socket 套接字
client = socket.socket()

# 创建连接
client.connect(('pic.bizhi360.com', 80))

# 构造 http 请求
http_req = 'GET ' + url + ' HTTP1.1\r\n' + \
    'Upgrade-Insecure-Requests: 1\r\n' + \
    'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1\r\n' +\
    '\r\n'

# 发送 http 请求
client.send(http_req.encode())

# 接收数据信息
data = client.recv(1024)

print(data)
