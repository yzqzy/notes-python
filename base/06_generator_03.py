from tools import line
from collections.abc import Iterable, Iterator

line()
# ---------------------

"""
生成器可以用函数实现，但不能通过函数实现迭代器

python 中，使用生成器可以很方便支持迭代器协议
yield 是一个语法糖, 内部支持迭代器协议, yield 内部是一个状态及，维护挂起和继续的状态
"""


def _range(num):
  i = 0

  while i < num:
    yield i
    i += 1


obj = _range(5)

print(next(obj))
print(next(obj))

print('----')

for i in obj:
  print(i)

line()
# ---------------------

"""
判定指定方法在指定类中是否实现
"""

print(hasattr(obj, '__iter__'))  # True
print(hasattr(obj, '__next__'))  # True
print(isinstance(obj, Iterable))  # True
print(isinstance(obj, Iterator))  # True

line()
# ---------------------

"""
生成器表达式
"""

tuple_data = (i for i in range(1, 11))

print(next(tuple_data))  # 1
print(hasattr(tuple_data, '__iter__'))  # True
print(hasattr(tuple_data, '__next__'))  # True

line()
# ---------------------

"""
send、close 方法

yield 可以返回值，也可以接受值
close 关闭生成器
"""


def _range(num):
  i = 0

  while i < num:
    recv_data = yield i
    print(f'range recv {recv_data}')
    i += 1


obj = _range(5)

# print(obj.send(None))  # 第一次使用 send 方法，信号值必须为 None，所以可以使用 next 进行驱动
print(next(obj))
print(obj.send('hello'))
print(obj.send('world'))
print(next(obj))
obj.close()

try:
  print(next(obj))
except StopIteration:
  print('error')

line()
# ---------------------

"""
协程和生成器有密不可分的关系
"""

line()
# ---------------------
