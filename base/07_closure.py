from tools import line

from abc import ABC, abstractmethod

line()
# ---------------------

"""
闭包

global: 声明全局变量可以在函数中使用
nolocal: 在内部函数中可以使用外部函数变量
"""


def counter(start=0):
  def add():
    nonlocal start
    start += 1
    return start

  return add


c1 = counter(5)

print(c1())  # 6
print(c1())  # 7
print(c1())  # 8


line()
# ---------------------

"""
Sequece 不可变序列、MutableSequence 可变序列

python 是基于协议编程的
  __getitem__: 序列协议
  __iter__: 迭代协议
  __contains__: in成员运算符协议
  __reversed__: 反转协议
"""


class MyList:
  def __init__(self, stu_list: list) -> None:
    self.stu_list = stu_list
    pass

  def __getitem__(self, v):
    return self.stu_list[v]


my_list = MyList([1, 2, 3])

print(my_list[0])  # 1
print(my_list[:2])  # [1, 2]

line()
# ---------------------

"""
__idadd__: 运算符协议

+= 调用的 __idadd__ 方法，本质调用 extend 方法
"""

int_data = [1, 2, 3]
c_data = int_data + [4, 5]

print(c_data)  # [1, 2, 3, 4, 5]
print(int_data)  # [1, 2, 3]

int_data += [4, 5]
print(int_data)  # [1, 2, 3, 4, 5]

line()
# ---------------------

"""
抽象基类
"""


class Cache(ABC):
  @abstractmethod
  def get_data(self):
    pass

  @abstractmethod
  def set_data(self, value):
    pass


class RedisCache(Cache):
  def get_data(self):
    pass

  def set_data(self, value):
    pass


redis_cache = RedisCache()
print(redis_cache)

line()
# ---------------------

"""
闭包应用场景: 装饰器
"""


def _wrapper(func):
  def wrapper(name):
    print('wrapper start')
    func(name)
  return wrapper


@_wrapper
def print_name(name):
  print(f'name {name}')


print_name('anna')
# wrapper start
# name anna

line()
# ---------------------
