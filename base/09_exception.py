from tools import line

line()
# ---------------------

"""
Exception 是所有错误类的基类

异常是 python 内部定义好的一些错误类

try:
  pass
except:
  pass
"""

# print(a)  # NameError: name 'a' is not defined

try:
  print(a)
except NameError:
  print('error')  # error

line()
# ---------------------


"""
如果可以确定错误种类，建议写上错误名称
"""


def exec_exception(x, y):
  try:
    result = x / y
    print(result)
  except ZeroDivisionError:
    print('error')


exec_exception(9, 3)  # 3.0
exec_exception(5, 0)  # error

line()
# ---------------------

"""
手动抛出异常

可以指定一个异常进行抛出，如果符合当前定义的异常，则可以执行其他的代码逻辑
"""

try:
  print('process')
  raise NameError
except:
  print('error')

"""
process
error
"""

line()
# ---------------------

"""
finally 一定会执行
"""

try:
  print('test')
  raise Exception
except:
  print('error')
else:
  print('process')
finally:
  print('finish')

line()
# ---------------------

"""
自定义异常

as 取别名
"""


class PassWordError(Exception):
  def __str__(self) -> str:
    return 'password failed'

  def __repr__(self) -> str:
    return '密码错误'


try:
  raise PassWordError()
except PassWordError as e:
  print(e)  # password failed

line()
# ---------------------
