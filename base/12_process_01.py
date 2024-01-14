import os
import time
import multiprocessing

# ---------------------

"""
创建进程

如果运行一个 py 文件, 操作系统会开启一个进程, 将 py 文件中的代码载入到内存
一旦操作系统开启一个进程, 会默认创建一个线程, 即主线程

进程创建的方式根据操作系统的不同而不同（使用进程最好使用 linux 系统）
1. windows swreap
2. linux fork
3. macos swreap

macos 和 windows 必须要写函数入口，才能使用进程
"""


def work_1():
  for i in range(5):
    print(f'work_1 {i}')
    time.sleep(1)


def work_2():
  for i in range(5):
    print(f'work_2 {i}')
    time.sleep(1)


p1 = multiprocessing.Process(target=work_1)
p2 = multiprocessing.Process(target=work_2)

# if __name__ == '__main__':
#   p1.start()
#   p2.start()

# ---------------------

"""
获取进程 pid
"""


def run_work():
  """ 子进程任务 """
  print(f'child process {os.getpid()}, parent process {os.getppid()}')


# if __name__ == '__main__':
#   print(f'main process {os.getpid()}')

#   p = multiprocessing.Process(target=run_work)
#   p.start()

# ---------------------

"""
进程方法及属性

Process
  args 元组方式传递参数
  kwargs 命名参数
  name 设定进程名称，可选
  group 指定进程组，大多数情况用不到（代码未实现）

  start 启动
  is_alive 判断子进程是否存活
  join 是否等待子进程执行结果，可以指定时间
  terminate 不管任务是否完成，立即终止子进程

  name 当前进程的别名
  pid  当前进程的 pid  
"""

# ---------------------

"""
进程之间不共享全局变量
"""

nums = [11, 22]


def work_1():
  for i in range(3):
    nums.append(i)
    time.sleep(1)
    print(f'work_1 {nums}')


def work_2():
  print(nums)
  print(f'work_2 {nums}')


if __name__ == '__main__':
  p1 = multiprocessing.Process(target=work_1)
  p2 = multiprocessing.Process(target=work_2)

  p1.start()
  p1.join()

  p2.start()

# ---------------------
