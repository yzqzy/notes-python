from tools import line
from collections.abc import Iterable, Iterator

line()
# ---------------------

"""
魔术方法 87 种

__iter__    迭代对象
__next__    迭代器对象
__getitem__ 序列对象
"""

line()
# ---------------------

"""
内置序列如何迭代

for 循环迭代过程中底层会执行 iter 方法，将迭代类型转为迭代器
"""

nums = [1, 2, 3]

print(isinstance(nums, Iterable))  # True
print(isinstance(nums, Iterator))  # False

iterObj = iter(nums)

print(iterObj)  # <list_iterator object at 0x102e822c0>
print(next(iterObj))  # 1
print(next(iterObj))  # 2
print(next(iterObj))  # 3

try:
  print(next(iterObj))
except StopIteration:
  print('stop')  # stop

line()
# ---------------------

"""
自定义迭代器
"""


class _List:
  def __init__(self) -> None:
    self.items = []

  def add(self, value):
    self.items.append(value)

  def __iter__(self):
    return _Iterator(self)


class _Iterator:
  def __init__(self, ins) -> None:
    self.listIns = ins
    self.current = 0

  def __next__(self):
    if self.current < len(self.listIns.items):
      item = self.listIns.items[self.current]
      self.current += 1
      return item
    else:
      raise StopIteration

  def __iter__(self):
    return self


list = _List()

list.add(1)
list.add(2)
list.add(3)

for item in list:
  print(item)

line()
# ---------------------

"""
迭代器代码优化
"""


line()
# ---------------------
