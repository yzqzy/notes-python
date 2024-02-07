import time
import pymongo
import requests

from urllib.parse import urlencode
from multiprocessing import Process, JoinableQueue as Queue

"""
多进程优化

多线程缺点: 存在 GIL 锁, 无法利用多核 CPU, 无法利用多线程提高 IO 密集型任务的处理速度
多线程优点: 适合 IO 密集型任务, 适合处理大量的并发请求

多进程缺点: 进程切换代价高, 内存占用高, 无法利用多核 CPU
多进程优点: 适合 CPU 密集型任务, 适合处理大量的短时任务

优化方案:
1. 多进程 + 协程: 利用多进程和协程实现 IO 密集型任务的并发处理
2. 多线程 + 协程: 利用多线程和协程实现 CPU 密集型任务的并发处理
3. 异步 IO: 利用异步 IO 实现 IO 密集型任务的并发处理
4. 多进程 + 异步 IO: 利用多进程和异步 IO 实现 IO 密集型任务的并发处理
5. 多线程 + 异步 IO: 利用多线程和异步 IO 实现 CPU 密集型任务的并发处理
"""

"""
多进程 + Queue 
"""

# 进程共享全局变量、不会互相影响
client = pymongo.MongoClient('localhost', 27017)
conn = client['spiders']['iqiyi_process']


class IqiyiSpider(Process):
  def __init__(self):

    self.url = 'https://pcw-api.iqiyi.com/search/recommend/list'
    self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Referer': 'https://list.iqiyi.com/'
    }

    self.url_queue = Queue()
    self.json_queue = Queue()
    self.content_queue = Queue()

  def get_url(self):
    params = {
        'channel_id': 1,
        'data_type': 1,
        'mode': 24,
        'page_id': 0,
        'ret_num': 48,
        'session': '0cfd980ce4504be879ab2915a539186c'
    }
    for page in range(1, 10):
      params['page_id'] = page
      self.url_queue.put(self.url + '?' + urlencode(params))

  def get_data(self):
    while True:
      url = self.url_queue.get()
      response = requests.get(url, headers=self.headers)
      self.json_queue.put(response.json())
      self.url_queue.task_done()

  def parse_data(self):
    while True:
      data = self.json_queue.get()
      for item in data['data']['list']:
        self.content_queue.put(item)
      self.json_queue.task_done()

  def save_data(self):
    while True:
      content = self.content_queue.get()
      conn.insert_one(content)
      self.content_queue.task_done()

  def create_process(self):
    process_list = []

    process_list.append(Process(target=self.get_url))

    for _ in range(5):
      process_list.append(Process(target=self.get_data))

    process_list.append(Process(target=self.parse_data))

    for _ in range(3):
      process_list.append(Process(target=self.save_data))

    return process_list

  def run(self):
    process_list = self.create_process()

    for p in process_list:
      p.daemon = True
      p.start()

    time.sleep(0.2)

    for q in [self.url_queue, self.json_queue, self.content_queue]:
      q.join()


if __name__ == '__main__':
  t1 = time.time()

  iqiyi = IqiyiSpider()
  iqiyi.run()

  print('总耗时：', time.time() - t1)  # 1.298255205154419

  # 比线程快
  # 1. 耗费资源比较多，创建也比较耗费资源
  # 2. 相比较，个人建议使用线程 + 队列
