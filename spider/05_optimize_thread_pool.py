import pymongo
import requests
import time

from queue import Queue
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor


# def get(url):
#   print(f'Getting {url}')
#   pass

# if __name__ == '__main__':
#   base_url = 'https://jobs.51job.com/pachongkaifa/p{}'
#   with ThreadPoolExecutor(max_workers=10) as executor:
#     for i in range(1, 20):
#       executor.submit(get, url=base_url.format(i))

# # ------------------------------


# def action(max):
#   """
#   计算指定数值的和
#   """
#   sum = 0
#   for i in range(max):
#     print(threading.current_thread().name + " " + str(i))
#     sum += i
#   return sum


# if __name__ == '__main__':
#   pool = ThreadPoolExecutor(max_workers=6)

#   future01 = pool.submit(action, 50)
#   future02 = pool.submit(action, 100)

#   # 判断future是否完成
#   print(future01.done(), future01.result())
#   print(future02.done(), future02.result())

#   # 关闭线程池
#   # pool.shutdown()


# # ------------------------------

"""
线程池优化

还可以使用队列继续优化，将任务放入队列，然后使用线程池执行队列中的任务。
"""


class Iqiyi(object):
  def __init__(self):
    self.client = pymongo.MongoClient('localhost', 27017)
    self.conn = self.client['spiders']['iqiyi_thread_pool']

    self.url = 'https://pcw-api.iqiyi.com/search/recommend/list'
    self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Referer': 'https://list.iqiyi.com/'
    }

  def get_data(self, page):
    params = {
        'channel_id': 1,
        'data_type': 1,
        'mode': 24,
        'page_id': page,
        'ret_num': 48,
        'session': '0cfd980ce4504be879ab2915a539186c'
    }
    response = requests.get(self.url, headers=self.headers, params=params)
    self.parse_data(response.json())
    print(f'第{page}页数据抓取完成')

  def parse_data(self, data):
    for item in data['data']['list']:
      self.save_data(item)
    pass

  def save_data(self, data):
    try:
      self.conn.insert_one(data)
    except Exception as e:
      print(e)

  def run(self):
    with ThreadPoolExecutor(max_workers=5) as executor:
      for page in range(1, 10):
        executor.submit(self.get_data, page)


if __name__ == '__main__':
  t1 = time.time()

  iqiyi = Iqiyi()
  iqiyi.run()

  print('总耗时：', time.time() - t1)  # 1.246415138244629


# # ------------------------------
