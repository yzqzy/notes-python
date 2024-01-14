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

loop = asyncio.get_event_loop()

tasks = [loop.create_task(func()) for _ in range(5)]
loop.run_until_complete(asyncio.wait(tasks))

print(f'all time {now() - start}')

# ---------------------


# ---------------------
