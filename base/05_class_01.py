def line():
  print('-' * 30)


line()
# ---------------------


def print_info(name, age):
  print(f'姓名: {name}, 年龄: {age}')


name = 'heora'
age = 20
print_info(name, age)  # 姓名: heora, 年龄: 20

line()
# ---------------------

"""
新式类
"""


class Student:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def print_info(self):
    print(f'姓名: {self.name}, 年龄: {self.age}')


stu = Student('heora', 20)
stu.print_info()  # 姓名: heora, 年龄: 20


line()
# ---------------------

"""

"""


class Teacher:
  def __init__(self, name) -> None:
    self.name = name

  @classmethod
  def print(cls):
    print(cls)

  def print_01(self):
    print(self, self.name)

  def print_02(self, name):
    print(self, name)


teacher = Teacher('heora')

teacher.print()  # <class '__main__.Teacher'>
teacher.print_01()  # <__main__.Teacher object at 0x102d41d90> heora
teacher.print_02('yueluo')  # <__main__.Teacher object at 0x1043c9fd0> yueluo

line()
# ---------------------
