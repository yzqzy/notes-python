import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
browser = webdriver.Chrome(service=service)

browser.get('https://www.baidu.com')

# 查询单个节点
el = browser.find_element(By.ID, 'kw')

# 输入关键字
el.send_keys('python')
# 模拟键盘操作
el.send_keys(Keys.ENTER)

time.sleep(3)

browser.quit()
