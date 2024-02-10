import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

"""
一些交互动作都是针对某个节点执行

对于输入框, 我们可以调用它的输入文字和清空文字方法
对于按钮，我们可以调用它的点击方法

但是有些时候，我们需要对多个节点执行动作，比如，我们需要先点击某个节点，然后再输入文字，或者先输入文字，然后再点击某个节点。
这时候, 我们就需要使用动作链ActionChains。
"""

service = webdriver.ChromeService(executable_path='./spider/driver/chromedriver')
browser = webdriver.Chrome(service=service)

browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

o_iframe = browser.find_element(By.XPATH, '//div[@id="iframewrapper"]/iframe')
browser.switch_to.frame(o_iframe)

o_draggable = browser.find_element(By.ID, 'draggable')
o_droppable = browser.find_element(By.ID, 'droppable')

ActionChains(browser).drag_and_drop(o_draggable, o_droppable).perform()

time.sleep(3)

browser.quit()
