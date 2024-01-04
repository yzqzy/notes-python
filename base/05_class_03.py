def line():
  print('-' * 30)


line()
# ---------------------

"""
重写: 子类定义与父类一样的方法

1. 解释器优先运行子类中的方法
2. 如果子类方法不存在，则寻找父类中的方法并运行
3. 如果父类不存在则报错
"""


class Father:
  def play_game(self):
    print('father method')


class Son(Father):
  def play_game(self):
    print('son method')


son = Son()
son.play_game()  # son method

line()
# ---------------------

"""
鸭子类型: 如果有一个动物，如果动物叫声像鸭子，走路像鸭子，则这个动物就是鸭子

python中所有的对象都是可以归类的;
python中对象都有一个所属的类型;

列表、字典、元组，只要支持迭代，它就是迭代类型，这其实就是鸭子类型。
鸭子类型在 python 源码中应用非常普遍。
"""

# say 方法是动物的特征


class Dog:
  def say(self):
    print('i am dog')


class Cat:
  def say(self):
    print('i am cat')


class Duck:
  def say(self):
    print('i am duck')


# animal = Dog
# animal().say()  # i am dog

# animal = Duck
# animal().say()  # i am duck

animal_list = [Dog, Cat, Duck]
for animal in animal_list:
  animal().say()

line()
# ---------------------
