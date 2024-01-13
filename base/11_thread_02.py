import time
import threading
import requests

from threading import RLock, Lock, Thread
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------------

"""
线程类完成爬虫功能

start:
  _bootstrap -> _bootstrap_inner
  负责线程启动等操作、调用 start
"""


class ThreadSpider(threading.Thread):
  def __init__(self, url) -> None:
    super().__init__()
    self.url = url

  def run(self) -> None:
    response = requests.get(self.url).content

    file_name = './base/imgs/' + self.url.split('/')[-1]

    with open(file_name, 'wb') as f:
      f.write(response)
      print('download success')


url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg',
]

# for url in url_list:
#   t = ThreadSpider(url)
#   t.start()

# ---------------------

"""
线程安全 资源竞争 线程锁

RLock 支持在同一个方法中上两把锁
  递归互斥锁
  多文件协同上锁, 保证文件内容正确性，避免资源竞争
  支持上下文协议, 性能相对 Lock 较差

Lock 
  普通互斥锁
  不支持，会产生死锁 
  不支持上下文协议、使用麻烦, 性能高
"""

num = 0
lock_obj = RLock()


# def add():
#   global num
#   for i in range(1000000):
#     lock_obj.acquire()
#     num += i
#     lock_obj.release()


# def sub():
#   global num
#   for i in range(1000000):
#     lock_obj.acquire()
#     num -= i
#     lock_obj.release()

def add():
  global num
  for i in range(1000000):
    with lock_obj:
      num += i


def sub():
  global num
  for i in range(1000000):
    with lock_obj:
      num -= i


# t1 = Thread(target=add)
# t2 = Thread(target=sub)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(num)

# ---------------------

"""
死锁

1. 普通互斥锁在上锁之前必须要保证当前锁的状态是解锁状态
2. 建议多个函数同时公用一个锁变量
3. 开发过程中尽量少用 Lock, 推荐使用 RLock
"""

num = 0
lock_obj = Lock()


def add():
  global num
  for i in range(1000000):
    lock_obj.acquire()
    lock_obj.acquire()
    num += i
    lock_obj.release()
    lock_obj.release()


def sub():
  global num
  for i in range(1000000):
    lock_obj.acquire()
    lock_obj.acquire()
    num -= i
    lock_obj.release()
    lock_obj.release()


# t1 = Thread(target=add)
# t2 = Thread(target=sub)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(num)

# ---------------------

"""
线程池

Future 是一种支持并发的对象

result  获取任务完成结果
done    判断任务是否完成
cancel  取消任务（受线程数、执行顺序影响）、任务一旦被线程绑定就无法被取消
"""


# def get_html(time_attr):
#   time.sleep(time_attr)
#   print(f'get current page content {time_attr}')
#   return time_attr


# pool = ThreadPoolExecutor(max_workers=2)

# task_1 = pool.submit(get_html, 3)
# task_2 = pool.submit(get_html, 2)

# print(task_2.cancel())  # False 如果任务数量少于 workers, 会取消失败

# print(task_1)  # <Future at 0x100856090 state=running>
# print(task_2)  # <Future at 0x10180c610 state=running>

# print(task_1.result())  # 3
# print(task_2.result())  # 2

# print(pool._max_workers)  # 2

# print(task_1.done())  # True
# print(task_2.done())  # True

# ---------------------

"""
线程池任务提交方式

as_completed 一个任务如果有返回值则直接返回, 类似生成器
map 必须等待任务完成之后才可以返回
"""


def get_html(time_attr):
  time.sleep(time_attr)
  print(f'get current page content {time_attr}')
  return time_attr


pool = ThreadPoolExecutor(max_workers=2)

""" 批量提交任务 as_completed """
# time_attr_list = [3, 2, 4, 1]
# all_task = [pool.submit(get_html, time_attr) for time_attr in time_attr_list]

# for future in as_completed(all_task):
#   print(future.result())

""" 批量提交任务 map """
time_attr_list = [3, 2, 4, 1]

for data in pool.map(get_html, time_attr_list):
  print(data)

# ---------------------
