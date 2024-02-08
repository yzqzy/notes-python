"""
自动化测试工具 Selenium

Selenium 是一个自动化测试工具，利用它可以驱动浏览器执行特定的动作，比如打开网页、输入内容、点击按钮、获取元素等。
还可以获取浏览器当前呈现的页面的源代码，可以做到可见即可爬。对于一些 javascript 驱动的页面，Selenium 也能做到自动化。
"""

import time

from selenium import webdriver

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.baidu.com')

time.sleep(3)

driver.quit()
