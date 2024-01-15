import time
import random
import asyncio

# ---------------------

"""
yield
"""


def func():
  print('generator func')

  while True:
    yield 'mock generate func data'


# gen_obj = func()

# print(next(gen_obj))
# print(next(gen_obj))

# ---------------------

"""
任务交替执行

1. 类似多线程并发效果
2. 最原始协程效果（python 2.7, python 3.4）
3. 任务切换之前必须指定切换的任务
"""


def func_a():
  while True:
    print('generator task')
    yield
    time.sleep(random.random())


def func_b(obj):
  while True:
    print('simple func')
    next(obj)


# func_b(func_a())

# ---------------------

"""
async 实现任务自动切换机制

协程可以提高同步任务效率 
"""


async def func():
  await asyncio.sleep(random.random())
  print('async task')

now = lambda: time.time()

start = now()

# loop = asyncio.get_event_loop()

# tasks = [loop.create_task(func()) for _ in range(5)]
# loop.run_until_complete(asyncio.wait(tasks))

# print(f'all time {now() - start}')

# ---------------------

"""
python 3.7 以上版本不需要我们手动创建事件循环，会在代码底层自动创建

下面使用 python 3.6 的语法创建协议对象，兼容 3.7

协程协议
  def __gaenter__(self):
    pass

minicoda3 python 环境
"""


async def work_1():
  for _ in range(5):
    print('task 1')
    await asyncio.sleep(random.random())


async def work_2():
  for _ in range(5):
    print('task 2')
    await asyncio.sleep(random.random())

loop = asyncio.get_event_loop()

# print(loop)  # <_UnixSelectorEventLoop running=False closed=False debug=False>

# coroutines = [
#     loop.create_task(work_1()),
#     loop.create_task(work_2())
# ]

# loop.run_until_complete(asyncio.wait(coroutines))

# ---------------------

"""
协程嵌套
"""


async def work_1():
  for _ in range(5):
    print('task 1')
    await asyncio.sleep(random.random())


async def work_2():
  for _ in range(5):
    print('task 2')
    await asyncio.sleep(random.random())


async def main():
  tasks = [work_1(), work_2()]
  await asyncio.gather(*tasks)

asyncio.run(main())

# ---------------------
