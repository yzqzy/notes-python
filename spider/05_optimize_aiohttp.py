import asyncio
import aiohttp
import time


"""
异步IO优化

aiohttp 是一个异步 HTTP 客户端/服务端框架，它基于 asyncio 实现。
aiomysql 异步操作 MySQL 数据库。
aiofiles 异步操作文件。
"""

"""
aiohttp 为 Python 提供异步 HTTP 客户端/服务端编程。基于 asyncio 的异步库。
asyncio 可以实现单线程并发 IO 操作，实现了 TCP、UDP、SSL 等协议, aiohttp 就是基于 asyncio 实现的 http 框架。

async 用来声明一个函数为异步函数, await 用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异步操作。
"""


async def request_data(client, i):
  await client.get('http://www.baidu.com')
  print(f"第{i+1}次请求完成")


# 总共耗时：1.3511850833892822秒
# async def main():
#   async with aiohttp.ClientSession() as client:
#     for i in range(30):
#       await request_data(client, i)

# 总共耗时：0.6430017948150635秒
async def main():
  async with aiohttp.ClientSession() as client:
    tasks = []
    for i in range(30):
      tasks.append(asyncio.create_task(request_data(client, i)))
    # await asyncio.gather(*tasks)
    await asyncio.wait(tasks)

if __name__ == '__main__':
  start_time = time.time()
  asyncio.run(main())
  print(f"总共耗时：{time.time() - start_time}秒")

"""
future

task 方法基于 future 对象，作用时判断当前事件循环中的任务状态

存在三种状态:
  PENDING: 任务尚未开始执行
  RUNNING: 任务正在执行
  DONE: 任务已执行完毕

task.done() 返回布尔值，表示任务是否已完成
task.result() 返回任务的结果，如果任务尚未完成，则会阻塞等待任务完成，并返回结果
task.cancel() 取消任务，如果任务尚未开始执行，则会直接返回 True，否则会尝试取消任务，并返回布尔值表示是否成功取消

asyncio.wait() 等待一组任务完成，并返回一个列表，列表中的元素是任务的结果
asyncio.gather() 等待一组任务完成，并返回一个列表，列表中的元素是任务的结果，与 asyncio.wait() 类似，但它会等待所有任务完成，而不管任务的执行顺序

asyncio.run() 运行一个协程，它会自动创建事件循环，并运行该协程，直到协程结束，并返回协程的结果。
asyncio.create_task() 创建一个任务，并返回该任务的 future 对象。
asyncio.sleep() 让当前任务暂停一段时间，并返回一个 future 对象。
"""
