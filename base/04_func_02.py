def line():
  print('-' * 30)


line()
# ---------------------

"""
缺省参数

数据库连接的三方库大量使用缺省参数
"""


def print_stu_info(name, age, gender, school='***'):
  print(name, age, gender, school)


print_stu_info('heora', 25, '男')

line()
# ---------------------

"""
命名参数

可以将对应的值绑定到对应的参数中
"""


def test(a, b):
  print(f'a={a}, b={b}')


test(1, 2)
test(a=2, b=1)

line()
# ---------------------

"""
不定长参数
"""


def test(a, b, *args, **kwargs):
  """
  :param a:
  :param b:
  :param args: 元组不定长，可省略
  :param kwargs: 字典不定长，可省略
  """
  print(f'a={a}, b={b}, *args={args}, **kwargs={kwargs}')


print(test.__doc__)

test(1, 2)  # a=1, b=2, *args=(), **kwargs={}
test(1, 2, 3, 4)  # a=1, b=2, *args=(3, 4), **kwargs={}
test(1, 2, 3, 4, name='heora')  # a=1, b=2, *args=(3, 4), **kwargs={'name': 'heora'}

"""
*args    不能在形参前面，建议在缺省参数后面
**kwargs 需要定义在所有参数后面
"""


def test_1(a, *args, b=2, **kwargs):
  print(f'args={args} a={a} b={b} kwargs={kwargs}')


test_1(1, 2, 3)  # args=(2, 3) a=1 b=2 kwargs={}
test_1(1, 2, 3, b=4)  # args=(2, 3) a=1 b=4 kwargs={}

line()
# ---------------------

"""
函数拆包：参数与值的个数以及位置要相同
"""


def test():
  return 1, 2, 3


a, b, c = test()
print(a, b, c)  # 1 2 3

ret = test()
print(ret[0], ret[1], ret[2])  # 1 2 3

"""
*  列表/字典/元组 拆包
** 字典拆包
"""


def test_1(a, b, c, d):
  print(a, b, c, d)


nums = [1, 2, 3, 4]
test_1(*nums)  # 1 2 3 4


def test(name, gender, address):
  print(name, gender, address)


info = {'name': 'heora', 'gender': 'male', 'address': 'china'}
test(**info)  # heora male china

line()
# ---------------------

"""
传递引用值
"""

nums = [1, 2, 3, 4]


def test(nums, num):
  nums.append(num)
  print(nums)


test(nums, 5)  # [1, 2, 3, 4, 5]


line()
# ---------------------
