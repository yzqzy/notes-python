import pymongo
import requests

"""
MongoDB 数据库
"""


class Iqiyi():
  def __init__(self):
    self.client = pymongo.MongoClient('localhost', 27017)
    self.conn = self.client['spiders']['iqiyi']

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
    for i in range(1, 10):
      self.get_data(i)
    print('数据抓取完成')


if __name__ == '__main__':
  iqiyi = Iqiyi()
  iqiyi.run()
