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

"""
类方法

classmethod cls 指向类对象，如果改动 class 名称，仍然可以使用 cls 获取类属性。
"""


class A:
  name = 'cls_a'

  @staticmethod
  def get_attr():
    print(A.name)

  @classmethod
  def get_attr_1(cls):
    print(cls.name)


a = A()
a.get_attr()  # cls_a
a.get_attr_1()  # cls_a

line()
# ---------------------

"""
* 强制指定传参
"""


class Person:
  def __init__(self, *, name, age) -> None:
    self.name = name
    self.age = age

  def info(self):
    print(self.name, self.age)


# person = Person(1, 2) # Person.__init__() takes 1 positional argument but 3 were given
person = Person(name='heora', age=25)
person.info()  # heora 25

line()
# ---------------------
