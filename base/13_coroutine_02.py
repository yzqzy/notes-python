import time
import random
import asyncio
import requests

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# ---------------------

"""
python 3.7 可以直接使用 run 方法自动创建一个事件循环

async 可以将一个普通函数包装成一个协程函数
      协程函数 + () = 协程函数

await 负责进行任务提交的一个接口
      如果提交任务类型是一个协程对象, 则需要等待协程对象返回值
      三个可传递的对象 协程对象、task 对象、future 对象

task 对象
      是对协程对象的进一步封装 已支持并发执行
      await 提交 task 任务，不会引起阻塞
"""


async def work():
  print('task running')
  await asyncio.sleep(random.random())
  return 'mock value'

# ------

# async def main():
#   tasks = [asyncio.create_task(work()) for _ in range(2)]

#   """
#   await 接收迭代对象并将迭代对象中的元素提交给事件循环，并获取被提交任务的运行状态

#   done: 已经完成的任务
#   pending: 未完成和正在执行的任务
#   """
#   done, pending = await asyncio.wait(tasks)

#   print(f'main {done}')  # {<Task finished name='Task-3' coro=<work() done, defined at /Users/heora/workspace/notes-python/base/13_coroutine_02.py:23> result='mock value'>, <Task finished name='Task-2' coro=<work() done, defined at /Users/heora/workspace/notes-python/base/13_coroutine_02.py:23> result='mock value'>}
#   print(f'main {pending}')  # main set()

#   for item in done:
#     print(f'item: {item.result()}')

# ------

# async def main():
#   tasks = [asyncio.create_task(work()) for _ in range(2)]

#   """
#   gather 只能接收单个对象，不能接收迭代对象，可以对迭代对象进行拆包
#   """
#   results = await asyncio.gather(*tasks)
#   print(results)

# ------


async def main():
  tasks = [asyncio.create_task(work()) for _ in range(2)]

  for item in asyncio.as_completed(tasks):
    print(await item)

# asyncio.run(main())

# ---------------------

"""
协程并发

future 类是 task 类的基类, task 对象只有运算得到返回值后, await 的对象才能传回值并且向下运行。
这个功能就是 future 对象来实现的。future 源码中存在一个 _state, 一旦 _state 值变成 finished, await 就不会继续等待。

future 偏向于底层，一般不会使用。
"""


async def work():
  delay = random.random()
  print('task is running')
  await asyncio.sleep(delay)
  return f'work value {delay}'


async def main():
  tasks = [asyncio.create_task(work()) for _ in range(2)]
  done, _ = await asyncio.wait(tasks)

  for item in done:
    print(item.result())

  return 'main value'

# value = asyncio.run(main())
# print(value)

# ---------------------

"""
future 异常处理

1. 获取不到值时, await 堵塞
2. awiat 解阻塞的前提是 future 对象有返回值
3. awiat 获取到返回值之后 future 的对象状态转为完成
"""


async def main():
  print('running')
  loop = asyncio.get_running_loop()  # 获取一个正在运行的事件循环
  fut = loop.create_future()  # 只创建对象, 没有绑定任务, 没有返回值
  # fut.set_result('mock value') # 设置返回值后 await 会解除阻塞
  await fut

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# ---------------------

"""
future 对象使用

低版本解释器可能会使用 (老版本写法, 3.5/3.6 使用比较多)
"""


async def work():
  print('work is running')
  await asyncio.sleep(1)
  return 'return value'


async def main():
  future_list = [asyncio.ensure_future(work()) for _ in range(2)]
  result_list = await asyncio.gather(*future_list)
  print(result_list)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# ---------------------

"""
线程和协程中的 future 对象

1. 两者没有关系，但是行为类似
2. task 对象中存在 result 方法
3. 使用方式基本一致
"""

# 这里的 future 和协程中的 future 没有任何关系
# from concurrent.futures import Future


def work(num):
  print('task is running')
  time.sleep(1)
  print(num)
  return 'return value'


# 创建线程池
# pool = ThreadPoolExecutor(max_workers=2)

# for _ in range(4):
#   fut = pool.submit(work, _)
#   print(fut)  # <Future at 0x1052136d0 state=running>
#   print(fut.result())  # return value

# 创建进程池
# if __name__ == '__main__':
#   pool = ProcessPoolExecutor(max_workers=2)

#   for _ in range(4):
#     fut = pool.submit(work, _)
#     print(fut.result())  # return value

# ---------------------

"""
交叉编程
"""


async def write(image_url, response):
  file_name = 'base/imgs/' + image_url.split('/')[-1]

  with open(file_name, 'wb') as f:
    f.write(response.content)


async def get_image(image_url):
  print(f'start download {image_url}')

  # 获取事件循环
  loop = asyncio.get_running_loop()
  # 默认创建线程池
  future = loop.run_in_executor(None, requests.get, image_url)

  # 创建的线程池返回的对象支持协程 await
  response = await future

  # 文件写入
  await write(image_url, response)

  print('download success')

url_list = [
    'http://pic.bizhi360.com/bbpic/98/10798.jpg',
    'http://pic.bizhi360.com/bbpic/92/10792.jpg',
    'http://pic.bizhi360.com/bbpic/86/10386.jpg',
]

# # 创建事件循环
# loop = asyncio.get_event_loop()
# tasks = [loop.create_task(get_image(url)) for url in url_list]
# # 执行任务
# loop.run_until_complete(asyncio.wait(tasks))

# ---------------------

"""
自定义支持异步迭代的类（自定义异步迭代器）
"""


class AsyncIter:
  def __init__(self) -> None:
    self.count = 0
    pass

  async def iter_num(self):
    await asyncio.sleep(random.random())
    self.count += 1
    if self.count == 100:
      return None
    return self.count

  # 异步迭代协议（只需要返回对象，并且返回对象不是耗时）
  def __aiter__(self):
    return self

  # next 获取下一个值之前可能遇到 io 等待
  async def __anext__(self):
    value = await self.iter_num()
    if value is None:
      raise StopAsyncIteration
    return value


async def iter_func():
  async for item in AsyncIter():
    print(item)

# asyncio.run(iter_func())

# ---------------------

"""
绑定回调
"""


async def work(name, gender):
  print(f'{name} {gender}')
  return f'return: {name}, {gender}'


def get_return(task_obj):
  print(f'{task_obj.result()}')


# # 创建事件循环
# loop = asyncio.get_event_loop()
# # 协程对象转为 task 对象
# task = loop.create_task(work('heora', 'male'))

# # res = loop.run_until_complete(task)
# # print(res)  # return: heora, male

# task.add_done_callback(get_return)
# loop.run_until_complete(task)

# ---------------------

"""
异步上下文管理器
"""


class AsyncContextManger:
  def __init__(self, conn=None) -> None:
    self.conn = conn
    pass

  async def get_data(self):
    return 'mock database crud'

  async def __aenter__(self):
    self.conn = await asyncio.sleep(random.random(), result='connect success')
    print(self.conn)
    return self

  async def __aexit__(self, exc_type, exc_val, exc_tb):
    await asyncio.sleep(2)
    print('close database success')


async def main():
  async with AsyncContextManger() as fp:
    result = await fp.get_data()
    print(result)

# asyncio.run(main())

# ---------------------

"""
uvloop

uvloop 是事件循环的替代方案，是一个三房库。使用 uvloop 可以在一定程序上提高事件循环的效率。
uvloop 事件循环 > 默认 asyncio 的事件循环效率，比其他框架效率至少可以提高两倍，性能可以比肩 go 语言。
windows 暂不支持 uvloop。
"""

# ---------------------
