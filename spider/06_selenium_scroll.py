import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
browser = webdriver.Chrome(service=service)

browser.get('https://github.com/yzqzy')

# 滚动到页面底部
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# 滚动到指定位置
browser.execute_script('window.scrollTo(0, 200);')

time.sleep(3)

browser.quit()
