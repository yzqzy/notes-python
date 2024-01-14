import time
import random

# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from multiprocessing import Process, Queue, Pool

# ---------------------

"""
队列

process 之间有时需要通信，操作系统提供了很多机制来实现进程间的通信，例如队列

可以给队列设置最大值，如果队列已满，会等待
"""

queue = Queue(2)

queue.put('msg_1')
queue.put('msg_2')

# print(queue.get())  # msg_1
# print(queue.get())  # msg_2

# print(queue.get())  # 如果队列为空，程序阻塞, 等待新任务
# print(queue.get_nowait()) # 抛出异常

"""
队列判断

empty 判断队列是否为空
full  判断队列是否已满
"""

# print(queue.empty())  # True
# print(queue.full())  # False

# ---------------------

"""
queue 实现多进程任务
"""


def write_data(queue):
  for item in 'ABC':
    queue.put(item)
    time.sleep(random.random())


def read_data(queue):
  while True:
    if not queue.empty():
      print(queue.get())
      time.sleep(random.random())
    else:
      break


def main():
  queue = Queue()

  p_write = Process(target=write_data, args=(queue,))
  p_read = Process(target=read_data, args=(queue,))

  p_write.start()
  p_write.join()

  p_read.start()
  p_read.join()

  print('exit')


# if __name__ == '__main__':
  # main()

# ---------------------

"""
进程池

1. 内置pool完成进程池创建
2. 进程池需要关闭(关闭当前进程池不再接收其他任务)

apply       同步执行任务
apply_async 异步执行任务
"""


def work(message):
  p_start = time.time()
  time.sleep(random.random() * 2)
  p_stop = time.time()
  print(f'msg {message}, time {p_stop - p_start}')


if __name__ == '__main__':
  main_start = time.time()

  pool = Pool(3)

  for i in range(10):
    # pool.apply(work, (i,))
    pool.apply_async(work, (i,))

  pool.close()
  pool.join()

  main_stop = time.time()

  print(f'main {main_stop - main_start}')

# ---------------------
