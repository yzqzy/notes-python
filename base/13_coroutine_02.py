import random
import asyncio

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
"""

# ---------------------
