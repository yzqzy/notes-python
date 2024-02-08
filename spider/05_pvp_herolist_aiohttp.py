import aiohttp
import asyncio
import os
import time

"""
使用 aiohttp 库爬取王者荣耀英雄列表，并下载英雄皮肤图片。
"""


class PvpSpider:
  def __init__(self):
    self.save_dir = 'spider/imgs/pvp'
    self.hero_url = 'https://pvp.qq.com/web201605/js/herolist.json'
    self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
    self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    pass

  async def get_hero_list(self, session):
    response = await session.get(self.hero_url, headers=self.headers, ssl=False)
    hero_list = await response.json(content_type=None)
    return hero_list

  async def get_image(self, session, ename, cname):
    for i in range(1, 10):
      response = await session.get(self.skin_url.format(ename, ename, i), ssl=False)
      if response.status == 200:
        content = await response.read()
        self.save_image(cname, i, content)
      else:
        break

  def save_image(self, cname, i, content):
    with open('{}/{}-{}.jpg'.format(self.save_dir, cname, i), 'wb') as f:
      f.write(content)
      print('save {}-{} success'.format(cname, i))

  async def run(self):
    if not os.path.exists(self.save_dir):
      os.makedirs(self.save_dir)

    async with aiohttp.ClientSession() as session:
      hero_list = await self.get_hero_list(session)

      tasks = []

      for hero in hero_list:
        ename = hero['ename']
        cname = hero['cname']
        tasks.append(
            asyncio.create_task(self.get_image(session, ename, cname))
        )

      await asyncio.wait(tasks)


if __name__ == '__main__':
  start_time = time.time()
  asyncio.run(PvpSpider().run())
  print('time: {}'.format(time.time() - start_time))
