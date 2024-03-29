from abc import ABC
from typing import Any

from tools import line

line()
# ---------------------

"""
装饰器

@ 装饰器语法糖

1. 调用外层函数获取内部函数的引用
2. 将内部函数引用赋值给一个变量
3. 使用变量运行内部函数
"""


def debug(func):
  def wrapper():
    print(f'[debug]: enter {func.__name__}')
    return func()
  return wrapper


@debug
def say_hello():
  print('hello')


@debug
def say_goodbye():
  print('hello')


say_hello()
say_goodbye()


line()
# ---------------------

"""
带参装饰器
"""


def my_wrapper(func):
  def _(msg):
    print(f'[before]: {msg}')
    return func(msg)
  return _


@my_wrapper
def say(msg):
  print(f'[msg]: {msg}')


say('hello world')

line()
# ---------------------

"""
有参数的定义方式
"""


def bug_level(level):
  def wrapper(func):
    def run_func(*args, **kwargs):
      print(f'bug {level}, run {func.__name__}')
      func(*args, **kwargs)
    return run_func
  return wrapper


@bug_level('info')
def say(name, msg):
  print(f'name={name}, msg={msg}')


say('heora', 'hello world')
"""
bug info, run say
name=heora, msg=hello world
"""

line()
# ---------------------

"""
基于类的装饰器

call: 可以染实例对象像函数一样被调用
"""


class Test:
  def __call__(self, *args: Any, **kwds: Any) -> Any:
    print('process')
    pass


t = Test()
t()  # process
t.__call__()  # process

line()
# ---------------------


class Logging:
  def __init__(self, func) -> None:
    self.func = func
    pass

  def __call__(self, *args: Any, **kwds: Any) -> Any:
    print(f'[debug]: {self.func.__name__}')
    self.func(*args, **kwds)


@Logging
def say(name, msg):
  print(f'name={name}, msg={msg}')


say('yueluo', 'hello world')
"""
[debug]: say
name=yueluo, msg=hello world
"""

line()
# ---------------------

"""
带参数类实现
"""


class Logging:
  def __init__(self, level='info') -> None:
    self.level = level
    pass

  def __call__(self, func) -> Any:
    def _(*args, **kwds):
      print(f'[{self.level}]: {func.__name__}')
      func(*args, **kwds)
    return _


@Logging(level='error')
def say(name, msg):
  print(f'name={name}, msg={msg}')


say('yueluo', 'hello world')
"""
[error]: say
name=yueluo, msg=hello world
"""

line()
# ---------------------

"""
装饰器总结
"""


class Test(ABC):
  @classmethod
  def info_01(cls):
    pass

  @staticmethod
  def info_02():
    pass

  # @abstractmethod
  # def info_03(self):
  #   pass

  # 将类方法作为属性使用
  @property
  def info_04(self):
    return 1


test = Test()

print(test.info_04)  # 1

line()
# ---------------------

"""
@property (鸡肋功能、框架底层可能会用)

1. 必须有返回值
2. 不允许有形参

页面分页，获取商品信息
"""


class Foo:
  def a(self):
    pass

  @property
  def b(self):
    pass

  @property
  def c(self):
    return '1'


foo = Foo()
print(foo.b)  # None
print(foo.c)  # 1


class Goods:

  @property
  def money(self):
    return 100


g = Goods()

res = g.money
print(res)  # 100


line()
# ---------------------

"""
分页处理
"""


class Page:
  def __init__(self, page) -> None:
    self.page = page
    self.page_size = 10
    pass

  @property
  def start(self):
    val = (self.page - 1) * self.page_size
    return val

  @property
  def end(self):
    val = self.page * self.page_size
    return val


page = Page(10)

print(page.start, page.end)  # 90 100

line()
# ---------------------

"""
骚操作
"""


class Goods:
  @property
  def price(self):
    print('property ')

  @price.setter
  def price(self, value):
    print(f'price setter {value}')

  @price.deleter
  def price(self):
    print('price deleter')


goods = Goods()

goods.price  # property
goods.price = 20  # price setter 20

del goods.price  # price deleter

line()
# ---------------------


class Goods:
  def __init__(self) -> None:
    self.origin_price = 100
    self.discount = 0.8
    pass

  @property
  def price(self):
    return self.origin_price * self.discount

  @price.setter
  def price(self, value):
    self.origin_price = value

  @price.deleter
  def price(self):
    del self.origin_price


goods = Goods()

print(goods.price)  # 80.0
goods.price = 200
print(goods.price)  # 160.0
# del goods.price
# print(goods.price) # AttributeError: 'Goods' object has no attribute 'origin_price'

line()
# ---------------------
