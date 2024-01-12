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
# for url in url_list:
#   t = threading.Thread(target=get_image, args=(url,))
#   t.start()

# ---------------------

"""
GIL锁

python 中存在全局解释器锁, 即 GIL。可以让一个进程在同一时刻只能有一个线程被执行。

例如在一个进程中创建多个线程, 在运行当前程序时在同一时刻只有一个线程被执行, 其他线程等待 cpu 调度。
这种情况无法利用多核 cpu 的优势, 如果想要绕开 GIL, 可以使用多进程的方式。
创建多个进程时，每个进程中只有一个线程。不过创建多进程消耗的资源比多线程消耗的资源大。

耗时的情况下, 并不会加速代码执行
"""

# ---------------------

"""
主线程与子线程的执行过程
"""


def work():
  for i in range(5):
    print(f'work {i}')
    time.sleep(1)


def main():
  t = threading.Thread(target=work)

  t.start()

  print('main processing...')


# if __name__ == '__main__':
#   main()

"""
work 0
main processing...
work 1
work 2
work 3
work 4
"""

# ---------------------

"""
线程方法

start: 启动线程
"""

num = 0


def add():
  global num
  for i in range(100000):
    num += i


# t = threading.Thread(target=add)
# t.start()

# print(num)

# ---------------------

"""
join: 主线程等待子线程任务完成之后执行主线程代码
"""


def add():
  for i in range(5):
    print(f'work {i}')
    time.sleep(1)


def main():
  t = threading.Thread(target=add)

  t.start()
  t.join()

  print('main process')


main()

# ---------------------

"""
"""

# ---------------------
