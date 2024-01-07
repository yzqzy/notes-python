from tools import line
from collections.abc import Iterable, Iterator

line()
# ---------------------

"""
像字典、列表等数据结构可以迭代，是因为实现了迭代协议
如果一个对象实现了 __iter__ 和 __next__ 方法，则当前对象就是一个迭代类型
"""

print(isinstance([], Iterable))  # True
print(isinstance({}, Iterable))  # True

line()
# ---------------------

"""
自定义迭代类型对象

可迭代对象
  底层实现迭代协议，但不一定实现迭代规则，没办法进行循环遍历

迭代器对象
  底层实现迭代规则，迭代器一定是迭代对象，但是迭代对象不一定是迭代器

from collections.abc import Iterable, Iterator
  Iterable: 迭代对象
  Iterator: 迭代器对象
"""


class Student:
  def __init__(self, stu_list) -> None:
    self.stu_list = stu_list
    pass

  # 魔术方法、用来添加类的一些行为特征
  def __iter__(self):
    pass


stu = Student([])
print(isinstance(stu, Iterable))  # True
print(isinstance(stu, Iterator))  # False

line()
# ---------------------

"""
迭代器

可迭代对象被称之为抽象基类

迭代类模板，任何类只要实现这个模板中的任意方法，这些类都能同一归为一类
"""

nums = [1, 2, 3]

iterator = iter(nums)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

line()
# ---------------------
