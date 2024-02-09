"""
自动化测试工具 Selenium

Selenium 是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，比如打开网页、输入内容、点击按钮、获取元素等。
还可以获取浏览器当前呈现的页面的源代码，可以做到可见即可爬。对于一些 javascript 驱动的页面, Selenium 也能做到自动化。

chromedriver 需要单独安装, 下载地址: https://chromedriver.chromium.org/downloads
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
browser = webdriver.Chrome(service=service)

browser.get('https://www.baidu.com')
browser.find_element(By.ID, 'kw').send_keys('javascript')
browser.find_element(By.ID, 'su').click()

# 打印页面源代码
# print(browser.page_source)

# 获取 cookie
# print(browser.get_cookies())

# 获取截屏
# time.sleep(3)
# browser.get_screenshot_as_file('baidu.png')

# 打印当前 URL
# print(browser.current_url)

time.sleep(3)

browser.quit()
