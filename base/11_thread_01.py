import time
import threading
import requests

"""
进程负责操作系统中的资源分配
线程使用资源、执行代码
"""

# ---------------------

"""
同步任务

多任务依次执行
"""


# def work_1():
#   for i in range(5):
#     print(f'work 1 {i}')
#     time.sleep(1)


# def work_2():
#   for i in range(5):
#     print(f'work 2 {i}')
#     time.sleep(1)


# work_1()
# work_2()

# ---------------------

"""
线程任务 并发执行
"""


def work_1():
  for i in range(5):
    print(f'work 1 {i}')
    time.sleep(1)


def work_2():
  for i in range(5):
    print(f'work 2 {i}')
    time.sleep(1)


t1 = threading.Thread(target=work_1)
t2 = threading.Thread(target=work_2)

# t1.start()
# t2.start()

# ---------------------

"""
线程爬虫
"""


def get_image(url):
  reponse = requests.get(url).content

  file_name = './base/imgs/' + url.split('/')[-1]

  with open(file_name, 'wb') as f:
    f.write(reponse)
    print('download success')
    time.sleep(1)


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg',
]

# 同步方式
# for url in url_list:
#   get_image(url)

# 线程方式
for url in url_list:
  t = threading.Thread(target=get_image, args=(url,))
  t.start()

# ---------------------
