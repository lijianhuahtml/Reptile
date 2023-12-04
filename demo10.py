from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# 节点交互
# Selenium 可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作。比较常见的用法有：输入文字时用 send_keys 方法，清空文字时用 clear 方法，点击按钮时用 click 方法。

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
input = browser.find_element(By.ID,'kw')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element(By.ID,'su')
button.click()
