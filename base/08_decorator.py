import inspect
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

line()
# ---------------------
