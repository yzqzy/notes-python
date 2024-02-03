import pymysql
import requests

"""
百度招聘
"""


class Baidu():
  def __init__(self):
    self.db = pymysql.connect(host='localhost', user='root', password='123456', database='spiders')
    self.cursor = self.db.cursor()

    self.url = 'https://talent.baidu.com/httservice/getPostListNew'
    self.headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': 'https://talent.baidu.com/jobs/social-list',
        'Cookie': 'your cookie'
    }

  def create_table(self):
    sql = '''
      CREATE TABLE IF NOT EXISTS baidu_jobs (
        id INT PRIMARY KEY AUTO_INCREMENT,
        education VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        service_condition TEXT
      )
    '''
    try:
      self.cursor.execute(sql)
      print('创建表成功')
    except Exception as e:
      print('创建表失败', e)

  def get_data(self, page):
    data = {
        'recruitType': 'SOCIAL',
        'pageSize': 10,
        'keyWord': 'python',
        'curPage': page,
        'projectType': ''
    }
    response = requests.post(self.url, headers=self.headers, data=data)
    return response.json()

  def parse_data(self, data):
    for item in data['data']['list']:
      education = item['education'] if item['education'] else ''
      name = item['name']
      service_condition = item['serviceCondition']
      self.save_data(education, name, service_condition)
    print('第{}页数据解析完成'.format(data['data']['pageNum']))
    pass

  def save_data(self, education, name, service_condition):
    sql = '''
      INSERT INTO baidu_jobs (education, name, service_condition)
      VALUES (%s, %s, %s)
    '''
    try:
      self.cursor.execute(sql, (education, name, service_condition))
      self.db.commit()
      print('保存数据成功')
    except Exception as e:
      self.db.rollback()
      print('保存数据失败', e)

    print('保存数据成功')

  def run(self):
    self.create_table()

    for i in range(1, 10):
      response = self.get_data(i)
      self.parse_data(response)


if __name__ == '__main__':
  baidu = Baidu()
  baidu.run()
