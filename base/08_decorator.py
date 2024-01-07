import inspect

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

line()
# ---------------------
