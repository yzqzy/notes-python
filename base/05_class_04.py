import export_class_test

from tools import line
from export_class_test import Father

# ---------------------

"""
调用其他文件方法
"""

obj = export_class_test.Father()
print(obj)

father = Father()
print(father)

line()
# ---------------------

"""
类属性

静态方法无法获取类属性
普通方法可以获取，不过也需要使用 self 进行访问

实例属性和类属性的区别：
1. 实例属性只能被实例对象访问
2. 类属性可以被实例对象和类对象访问
"""


class Father:
  gender = '男'

  def __init__(self, name) -> None:
    self.name = name

  def info(self):
    print(f'name {self.name}, gender {self.gender}')


father = Father('heora')
father.info()  # name heora, gender 男

line()
# ---------------------
