import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
嵌套 iframe
"""

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
browser = webdriver.Chrome(service=service)

browser.get('https://www.douban.com/')

o_iframe = browser.find_element(By.XPATH, '//div[@class="login"]/iframe')

browser.switch_to.frame(o_iframe)
browser.find_element(By.NAME, 'phone').send_keys('13812345678')

time.sleep(2)

browser.quit()
