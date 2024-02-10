import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

# 隐藏正在受到自动化测试软件控制的提示
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option("excludeSwitches", ['enable-automation'])

# 拓展 chrome 插件
# options.add_extension('./spider/driver/tampermonkey.crx')

# 设置 proxy 代理
# options.add_argument('--proxy-server=http://127.0.0.1:7890')

# 禁用图片
# options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})

# 无头模式，后台运行
# options.add_argument('--headless')

# 设置 use-agent，手机
# options.add_argument(
#     'user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
browser = webdriver.Chrome(service=service, options=options)

# 设置浏览器最大化
# browser.maximize_window()

# 设置浏览器窗口大小
# browser.set_window_size(768, 1024)

browser.get('https://www.4399.com/flash/')

# 通过 js 打开新页面
# browser.execute_script("window.open('https://www.baidu.com')")

time.sleep(3)

browser.quit()
