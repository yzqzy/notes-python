from tools import line

line()
# ---------------------

"""
open 函数

mode 文件模式
r: 文件只能读取
w: 文件只能写入
a: 表示打开文件，在原有内容基础上追加内容，末尾追入
w+: 表示可以对文件进行读写双重操作

mode 二进制常用模式
rb:  以二进制格式打开一个文件，用于只读
wb:  以二进制格式打开一个文件，用于只写
ab:  以二进制格式打开一个文件，用于追加
wb+: 以二进制格式打开一个文件，用于读写
"""

file_name = './base/export_class_test.py'
file_obj = open(file_name, encoding="utf8")

print(file_obj)  # <_io.TextIOWrapper name='./base/export_class_test.py' mode='r' encoding='UTF-8'>
print(file_obj.name)  # ./base/export_class_test.py
print(file_obj.mode)  # r

"""
读取文件时可能会出现乱码情况

假设windows读取文件乱码, 可以使用 GBK 模式
"""

print(file_obj.read())

line()
# ---------------------

"""
文件写入

完成读写操作之后，需要关闭文件对象
"""

file_name = './base/test.txt'

file_obj = open(file_name, mode='w')
file_obj.write('test test test\n')

file_obj = open(file_name, mode='a')
file_obj.write('test test tesn\n')
file_obj.write('test test test\n')

file_obj.close()  # close file obj

line()
# ---------------------

"""
读写行
"""

file_name = './base/test.txt'
file_obj = open(file_name)

# result = file_obj.readline()
# print(result)

""" 读写整个文件、并输出列表数据 """
result = file_obj.readlines()
print(result)

file_obj.close()

""" 写入列表 """

file_obj = open(file_name, 'a')

name_list = ['heora\n', 'yueluo\n']
file_obj.writelines(name_list)

file_obj.close()

file_obj = open(file_name, 'r')
result = file_obj.readlines()
print(result)

file_obj.close()

line()
# ---------------------

"""
w+ 需要知道文件游标对象，不建议使用

推荐使用 a、r
"""

line()
# ---------------------

"""
with 上下文管理器

1. enter 遇到 with 关键字会自动执行
2. python 解释器一旦跳出当前代码块，会执行 exit 方法

enter 数据库连接
exit  数据库断开连接

可以用来管理数据库的连接和断开操作
"""


class Student:
  def __enter__(self):
    print(1)

  def __exit__(self, exc_type, exc_val, exc_tb):
    print(2)


with Student() as stu:
  pass

line()
# ---------------------

"""
with 控制打开操作

open 方法底层实现上下文协议，可以自动执行 close 方法
"""

with open('./base/test.txt') as file_obj:
  print(file_obj.read())

"""
test test test
test test tesn
test test test
heora
yueluo
"""

line()
# ---------------------

"""
open
"""


class OpenFile:
  def __init__(self) -> None:
    self.file_obj = None
    pass

  def __enter__(self):
    print(1)
    self.file_obj = open('./base/test.txt')
    return self

  def my_read(self):
    print(self.file_obj.read())

  def __exit__(self, exc_type, exc_val, exc_tb):
    print(2)
    self.file_obj.close()


with OpenFile() as file:
  print(file.file_obj.read())

line()
# ---------------------
