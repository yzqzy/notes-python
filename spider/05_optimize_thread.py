import pymongo
import requests
import time

from queue import Queue
from urllib.parse import urlencode
from threading import Thread

"""
多线程 + Queue 优化爬虫
"""


class Iqiyi(object):
  def __init__(self):
    self.client = pymongo.MongoClient('localhost', 27017)
    self.conn = self.client['spiders']['iqiyi_threads']

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
      self.conn.insert_one(content)
      self.content_queue.task_done()

  def create_theads(self):
    thread_list = []

    thread_list.append(Thread(target=self.get_url))

    for _ in range(3):
      thread_list.append(Thread(target=self.get_data))

    thread_list.append(Thread(target=self.parse_data))

    thread_list.append(Thread(target=self.save_data))

    return thread_list

  def run(self):
    # 创建线程池
    thread_list = self.create_theads()

    for t in thread_list:
      # 设置为守护线程，主线程结束时自动结束
      t.daemon = True
      # 启动线程
      t.start()

    for i in [self.url_queue, self.json_queue, self.content_queue]:
      # 主线程阻塞，等待队列中所有任务完成
      i.join()


if __name__ == '__main__':
  t1 = time.time()

  iqiyi = Iqiyi()
  iqiyi.run()

  print('总耗时：', time.time() - t1)  # 1.674206018447876
