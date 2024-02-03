import pymysql

"""
MySQL 数据库
"""


def select_version(cursor):
  cursor.execute('SELECT VERSION()')
  data = cursor.fetchone()
  print('Database version:', data)


def show_databases(cursor):
  cursor.execute('SHOW DATABASES')
  data = cursor.fetchall()
  print('Databases:', data)


def create_database_spiders(cursor):
  cursor.execute('CREATE DATABASE  IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
  pass


def db_connect():
  # 连接数据库
  db = pymysql.connect(host='localhost', user='root', password='123456')
  # 创建游标
  cursor = db.cursor()

  # 查询数据库版本
  select_version(cursor)
  # 创建数据库（设置编码集、排序规则、数据库名称）
  create_database_spiders(cursor)
  # 查看数据库
  show_databases(cursor)

  # 关闭数据库连接
  db.close()


def main():
  db_connect()
  pass


if __name__ == '__main__':
  main()
