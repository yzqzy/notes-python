def line():
  print('-' * 30)


line()
# ---------------------

"""
私有属性 (__): 
1. 外部无法访问、无法修改
2. 內部可以访问、

有一种方法可以访问，不建议使用
1. _类名__属性名
2. _类名__私有方法名
"""


class Dog:
  def __init__(self, name, age) -> None:
    self.__name = name
    self.__age = age

  def info(self):
    print(f'name: {self.__name}, age: {self.__age}')

  def set_age(self, age):
    self.__age = age


dog_1 = Dog('哈士奇', 3)
dog_1.info()  # name: 哈士奇, age: 3

dog_2 = Dog('金毛', 2)
dog_2.set_age(3)
dog_2.info()  # name: 金毛, age: 3

print(dog_1._Dog__name)  # 哈士奇

line()
# ---------------------

"""
对象关联
"""


class ClassRoom:
  def __init__(self, name) -> None:
    self.cls_room = name
    self.stu_list = list()

  def add_stu(self, stu):
    self.stu_list.append(stu)


class Student:
  def __init__(self, name) -> None:
    self.stu_name = name


cls_01 = ClassRoom('cls 1')

stu_01 = Student('heora')
stu_02 = Student('yueluo')

cls_01.add_stu(stu_01)
cls_01.add_stu(stu_02)

for stu in cls_01.stu_list:
  print(stu.stu_name)

line()
# ---------------------

"""
对象继承

1. 私有属性无法继承
2. 私有方法无法被继承
"""


class Animal:
  def run(self):
    print('run...')

  def play(self):
    print('play...')


# 继承
class Dog(Animal):
  pass


dog = Dog()

dog.run()
dog.play()

line()
# ---------------------

"""
多继承
"""


class Camera:
  def take_photo(self):
    print('拍照...')


class Movie:
  def play_movie(self):
    print('看电影...')


class Phone(Camera, Movie):
  pass


phone = Phone()

phone.play_movie()  # 看电影...
phone.take_photo()  # 拍照...

line()
# ---------------------

"""
type object class

所有的对象都是由同一个对象创建的

实例对象是类创建的
type 创建一切、包括自己, type 本质是一个指针
"""
